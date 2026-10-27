import base64, hashlib, io, pathlib, re, sys, zipfile
source = pathlib.Path(sys.argv[1])
target = pathlib.Path(sys.argv[2]).resolve()
text = source.read_text(encoding="utf-8")
match = re.search(r"<!-- ARCHIVE_BASE64_BEGIN -->\s*```base64\s*(.*?)\s*```\s*<!-- ARCHIVE_BASE64_END -->", text, re.S)
if not match:
    raise SystemExit("Archive block missing or truncated")
data = base64.b64decode("".join(match.group(1).split()), validate=True)
expected = re.search(r"Archive-SHA256: ([0-9a-f]{64})", text).group(1)
if hashlib.sha256(data).hexdigest() != expected:
    raise SystemExit("Archive checksum mismatch")
with zipfile.ZipFile(io.BytesIO(data)) as archive:
    for item in archive.infolist():
        path = pathlib.PurePosixPath(item.filename)
        if path.is_absolute() or ".." in path.parts or "\\" in item.filename or ":" in item.filename:
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
