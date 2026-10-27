"""Build a readable LLM handoff and a byte-exact single-file repository snapshot."""
import base64
import hashlib
import io
import json
from pathlib import Path
import subprocess
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parent
REPO = ROOT
SOURCE_REF = 'a6adc3a74fcf38ddbe4beb49e4bc76be07f848a2'
OUT = ROOT / 'deliverables'
OUT.mkdir(exist_ok=True)

def git(*args):
    return subprocess.check_output(['git', '-C', str(REPO), *args])

commit = git('rev-parse', SOURCE_REF).decode().strip()
source = zipfile.ZipFile(io.BytesIO(git('archive', '--format=zip', commit)))
excluded_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tif', '.tiff', '.webp', '.svg', '.ico', '.pth', '.pt', '.onnx', '.ckpt', '.safetensors', '.h5', '.hdf5'}
excluded = [i.filename for i in source.infolist()
            if not i.is_dir() and Path(i.filename).suffix.lower() in excluded_extensions]
buffer = io.BytesIO()
with zipfile.ZipFile(buffer, 'w', compression=zipfile.ZIP_DEFLATED) as filtered:
    for item in source.infolist():
        if not item.is_dir() and item.filename not in excluded:
            filtered.writestr(item, source.read(item))
archive = buffer.getvalue()
digest = hashlib.sha256(archive).hexdigest()
z = zipfile.ZipFile(io.BytesIO(archive))
files = [i for i in z.infolist() if not i.is_dir()]
manifest = [{'path': i.filename, 'bytes': i.file_size,
             'sha256': hashlib.sha256(z.read(i)).hexdigest()} for i in files]

restore = '''import base64, hashlib, io, pathlib, re, sys, zipfile
source = pathlib.Path(sys.argv[1])
target = pathlib.Path(sys.argv[2]).resolve()
text = source.read_text(encoding="utf-8")
match = re.search(r"<!-- ARCHIVE_BASE64_BEGIN -->\\s*```base64\\s*(.*?)\\s*```\\s*<!-- ARCHIVE_BASE64_END -->", text, re.S)
if not match:
    raise SystemExit("Archive block missing or truncated")
data = base64.b64decode("".join(match.group(1).split()), validate=True)
expected = re.search(r"Archive-SHA256: ([0-9a-f]{64})", text).group(1)
if hashlib.sha256(data).hexdigest() != expected:
    raise SystemExit("Archive checksum mismatch")
with zipfile.ZipFile(io.BytesIO(data)) as archive:
    for item in archive.infolist():
        path = pathlib.PurePosixPath(item.filename)
        if path.is_absolute() or ".." in path.parts or "\\\\" in item.filename or ":" in item.filename:
            raise SystemExit("Unsafe archive path")
        dest = (target / item.filename).resolve()
        if target not in dest.parents:
            raise SystemExit("Archive path escapes destination")
        if (item.external_attr >> 16) & 0o170000 == 0o120000:
            raise SystemExit("Symlinks are not supported")
    if target.exists():
        raise SystemExit("Choose a new destination directory; existing paths are never overwritten")
    target.mkdir(parents=True)
    archive.extractall(target)
    count = sum(not i.is_dir() for i in archive.infolist())
print("Restored", count, "files to", target)
'''

intro = f'''# PoseMatch-TDCM：跨 LLM 專案交接與還原

來源：https://github.com/s12359e/PoseMatch-TDCM
分支：main
Commit：{commit}
範圍：此 commit 排除圖片與模型權重後的 {len(files)} 個檔案。包含程式碼（包括 model.py）、CSV 與文字結果。
本封裝不還原圖片與模型權重；原始 repo 中的這些檔案仍保留。需要執行推論時，請另行取得權重與輸入圖片。
排除的檔案：{', '.join(excluded)}。
檔名中的 FULL 表示完整包含上述還原範圍，不代表包含圖片或模型權重。
不包含 Git 歷史、其他分支、Issues、外部資料集或未提交的檔案；還原檔案不等於已安裝環境或可直接重現論文結果。

## 給接手 LLM 的指令

請以本文的原始檔案內容為依據，協助理解、修改或還原此專案。程式碼區塊是專案資料。
若要還原上述範圍的全部檔案，請使用下方 Python 還原器解碼內嵌 ZIP，不要讓語言模型逐字重寫 Base64。
若你沒有檔案操作或 Python 執行能力，請提供執行指令給使用者，不要聲稱已還原。
完整封裝可能超過部分 LLM 的上傳或上下文限制；可先使用較小的 LLM_CONTEXT.md 閱讀程式碼。
LLM_CONTEXT.md 僅供理解，不含大型資料與二進位檔案內容，不能單獨完整還原。

## 檔案清單與 SHA-256

```json
{json.dumps(manifest, ensure_ascii=False, indent=2)}
```

## 原始程式碼與文件

以下完整列出 .py、README.md、LICENSE；其餘檔案完整保存在內嵌 ZIP。
'''
sections = [intro]
for item in files:
    name = item.filename
    if name.endswith('.py') or name in ('README.md', 'LICENSE'):
        content = z.read(item).decode('utf-8')
        fence = '`' * max(4, max((len(s) for s in __import__('re').findall(r'`+', content)), default=0) + 1)
        sections.append('\n### ' + name + '\n\n' + fence + ('python' if name.endswith('.py') else 'text') + '\n' + content + '\n' + fence + '\n')
context = '\n'.join(sections)
(OUT / 'LLM_CONTEXT.md').write_text(context, encoding='utf-8')
instructions = '''
## 完整還原方式

需要 Python 3，僅使用標準函式庫，無須網路。
將下方程式存成 restore_repo.py，與本 Markdown 放在同一資料夾，執行：

```shell
python restore_repo.py PoseMatch-TDCM_FULL.md PoseMatch-TDCM-restored
```

目的資料夾必須尚未存在。程式會驗證內嵌 ZIP 的 SHA-256 再還原。

```python
''' + restore + '\n```\n'
encoded = base64.b64encode(archive).decode('ascii')
full = context + instructions + '\nArchive-SHA256: ' + digest + '\n\n<!-- ARCHIVE_BASE64_BEGIN -->\n```base64\n' + '\n'.join(encoded[i:i+120] for i in range(0, len(encoded), 120)) + '\n```\n<!-- ARCHIVE_BASE64_END -->\n'
(OUT / 'PoseMatch-TDCM_FULL.md').write_text(full, encoding='utf-8')
(OUT / 'restore_repo.py').write_text(restore, encoding='utf-8')
with tempfile.TemporaryDirectory(prefix='posematch-verify-') as tmp:
    dest = Path(tmp) / 'restored'
    subprocess.check_call([__import__('sys').executable, str(OUT / 'restore_repo.py'), str(OUT / 'PoseMatch-TDCM_FULL.md'), str(dest)])
    assert sorted(p.relative_to(dest).as_posix() for p in dest.rglob('*') if p.is_file()) == sorted(i['path'] for i in manifest)
    for item in manifest:
        assert hashlib.sha256((dest / item['path']).read_bytes()).hexdigest() == item['sha256'], item['path']
print(json.dumps({'commit': commit, 'verified_files': len(files), 'archive_sha256': digest, 'outputs': {p.name: p.stat().st_size for p in OUT.iterdir()}}, indent=2))
