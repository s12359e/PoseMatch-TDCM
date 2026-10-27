# PoseMatch-TDCM：跨 LLM 專案交接與還原

來源：https://github.com/s12359e/PoseMatch-TDCM
分支：main
Commit：a6adc3a74fcf38ddbe4beb49e4bc76be07f848a2
範圍：此 commit 排除圖片與模型權重後的 19 個檔案。包含程式碼（包括 model.py）、CSV 與文字結果。
本封裝不還原圖片與模型權重；原始 repo 中的這些檔案仍保留。需要執行推論時，請另行取得權重與輸入圖片。
排除的檔案：dict/model.pth, framework.png, res/image.png, res/result.png, res/template.png。
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
[
  {
    "path": "LICENSE",
    "bytes": 1087,
    "sha256": "d4234887a85dfc44424d3fdb385edf545cdf87d11b639a2711b43b3a0042db5f"
  },
  {
    "path": "README.md",
    "bytes": 2005,
    "sha256": "231708bcb44a7b948ca28905de424feb7b6e361e9cc053d8d3fd9b9451d2be93"
  },
  {
    "path": "data/DOTA.py",
    "bytes": 10948,
    "sha256": "4e099be5d12a16d858a8ea81f226e0bf7c63c969ef63dbc74b5373999ecab77a"
  },
  {
    "path": "data/S2/train.csv",
    "bytes": 6847096,
    "sha256": "c503cd5dee83c60d89217c415d32d1dbb0157dd2be9414957b94f346fd5e21a2"
  },
  {
    "path": "data/S2/val.csv",
    "bytes": 298486,
    "sha256": "e723dd50166aeb5519c8aadc41c925c522c16025ac73f91d98f932a40f64c945"
  },
  {
    "path": "data/filterData.py",
    "bytes": 2797,
    "sha256": "1d46c24734c3aa69b5f498ceddfeff1f6028aec085e68146a23bfb1e35fd1909"
  },
  {
    "path": "model.py",
    "bytes": 6337,
    "sha256": "fef8b3acaa93f3593b057632de3343f230adc7bca6bdacad5acd4402b9a8b2ad"
  },
  {
    "path": "res/result-multi.txt",
    "bytes": 2327466,
    "sha256": "0344ddb6e84d9817ec8568b5bbc03d3b3474932fd8a75be82c20bc33728c8e62"
  },
  {
    "path": "res/result-single.txt",
    "bytes": 313227,
    "sha256": "fc246d124c2782273007cb071202b01788ffdc6ba318372590e2c72e26a1541b"
  },
  {
    "path": "test.py",
    "bytes": 3778,
    "sha256": "01277f753e73d40d7054628c8fe592f26741d6e9fa533a543ff46e461b713b97"
  },
  {
    "path": "test_single.py",
    "bytes": 6329,
    "sha256": "520d19e57d88a3f7e14790fe04d368d7f0cab4b668562654eada19376b1a5d66"
  },
  {
    "path": "train.py",
    "bytes": 8335,
    "sha256": "a5a21c92c4b5ceaaaaa6277f2a31696a4062ba299af202566a9f74ef7852ab83"
  },
  {
    "path": "utils/__init__.py",
    "bytes": 446,
    "sha256": "83f529694cb80abc116808ab9e3265216cf07a023868853949784b677849d41d"
  },
  {
    "path": "utils/dataSet.py",
    "bytes": 2340,
    "sha256": "b17a5f740cfd54e11ab30c70439ea2195ea57f48adbf3deda86bedc1a27bc48f"
  },
  {
    "path": "utils/get_imgR.py",
    "bytes": 9263,
    "sha256": "cd78812b29877073321cf9a2ca4a9181880e80b26a4011e743c794cde0f47fe1"
  },
  {
    "path": "utils/loss.py",
    "bytes": 2690,
    "sha256": "19d9d355dd68e975d3e6495f51b231108bbc99033d4c045a3c687ac00a16651a"
  },
  {
    "path": "utils/refine.py",
    "bytes": 10396,
    "sha256": "f015f3daf7a13cc3152ed2fff356b9d3909b5e7bff9c9b271cdddf91020d1cf0"
  },
  {
    "path": "utils/tool.py",
    "bytes": 5451,
    "sha256": "9be62ee185dd66e16f86cda60e36509dbe3a1cb4ba8266d418fe8977b476a09c"
  },
  {
    "path": "utils/tools.py",
    "bytes": 4703,
    "sha256": "47f2856cb1524b033bff983d6580d8fdca6a831e5a7d6627ab84963e81ae2789"
  }
]
```

## 原始程式碼與文件

以下完整列出 .py、README.md、LICENSE；其餘檔案完整保存在內嵌 ZIP。


### LICENSE

````text
MIT License

Copyright (c) 2025 ZhouJ6610

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

````


### README.md

````text
# PoseMatch-TDCM

This repository provides the official implementation of our paper:

**"An Efficient Deep Template Matching and In-Plane Pose Estimation Method via Template-Aware Dynamic Convolution"**  
*Published in **Expert Systems with Applications***

## 🔧 Framework Architecture

![Framework](framework.png)



## 🔍 Highlights

• End-to-end estimation of 2D geometric pose for planar template matching.  
• TDCM enables strong generalization to unseen targets with efficient matching.  
• Compact 3.07M model achieves robust matching and real-time speed under transformations.  
• A refinement module improves angle-scale estimation via local geometric fitting.  
• Structure-aware pseudo labels enable self-supervised training without annotations.  

## 🚀 Matching Performance
All results are based on a standard template size of **36×36**, unless otherwise specified.

| Setting   | Description                          | Precision (mIoU ↑) | Time(i9-14900KF CPU) ↓ |
| --------- | ------------------------------------ | :----------------: | :-----------------:    |
| **S1**    | Rotation only                        |     **0.955**      |     **11.3 ms**        |
| **S1.5**  | Rotation + mild scaling (0.8–1.5×)   |     **0.926**      |     **13.8 ms**        |
| **S2**    | Rotation + moderate scaling (0.5–2×) |     **0.900**      |     **14.2 ms**        |
| **S2.5**  | Rotation + large scaling (0.4–2.5×)  |     **0.897**      |     **14.7 ms**        |


## 🖥️ Usage

`test.py` contains example usage of the PoseMatch-TDCM matcher.  
To try with your own images, edit the file and set:

```python
query_image_path = './res/image.jpg'
template_image_path = './res/template.jpg'

# true_param: center(x,y) scale_x(tw / 36), scale_y(th / 36), angle
# Please ensure that the size of the template image is between 18 and 72.
true_param = np.array([47.47,67.61,0.89,1.31,-78.53], dtype=np.float32)
```
   


````


### data/DOTA.py

````python
import cv2
import numpy as np
import os
import glob
import math
from PIL import Image

'''
构建DOTA模板匹配测试集
'''

def draw_polygon(image, points, color, thickness=2):
    """在图像上绘制多边形"""
    int_points = np.array([[int(p[0]), int(p[1])] for p in points], dtype=np.int32)
    cv2.polylines(image, [int_points], isClosed=True, color=color, thickness=thickness)
    return image

def calculate_min_area_rect_angle(corners):
    """使用最小外接矩形计算旋转角度"""
    corners_array = np.array(corners, dtype=np.float32)
    rect = cv2.minAreaRect(corners_array)
    return rect[2]  # 返回旋转角度

def calculate_rotation_angle(corners):
    """根据模板坐标计算旋转角度 - 改进版"""
    if len(corners) < 4:
        return 0
    
    # 方法1: 使用最小外接矩形计算角度
    min_area_angle = calculate_min_area_rect_angle(corners)
    
    # 方法2: 计算两条长边的角度并取平均
    edges = []
    for i in range(4):
        dx = corners[(i+1)%4][0] - corners[i][0]
        dy = corners[(i+1)%4][1] - corners[i][1]
        length = math.sqrt(dx**2 + dy**2)
        angle = math.degrees(math.atan2(dy, dx))
        edges.append((length, angle))
    
    # 按长度排序，取最长的两条边
    edges.sort(key=lambda x: x[0], reverse=True)
    long_edge_angles = [edges[0][1], edges[1][1]]
    
    # 计算平均角度
    avg_angle = np.mean(long_edge_angles)
    
    # 选择最稳定的角度计算方法
    # 使用最小外接矩形的角度，但调整到-90——90度范围
    if min_area_angle < -45:
        min_area_angle += 90
    elif min_area_angle > 45:
        min_area_angle -= 90
    
    return min_area_angle

def rotate_point(point, center, angle_deg):
    """旋转点坐标（围绕中心点，与OpenCV旋转方向一致）"""
    angle_rad = np.deg2rad(angle_deg)
    x, y = point
    cx, cy = center
    
    # 平移点到原点
    x -= cx
    y -= cy
    
    # 旋转
    x_rot = x * np.cos(angle_rad) + y * np.sin(angle_rad)
    y_rot = -x * np.sin(angle_rad) + y * np.cos(angle_rad)
    
    # 平移回原位置
    x_rot += cx
    y_rot += cy
    
    return (x_rot, y_rot)

def process_template_data(image, template_corners):
    """处理模板数据：旋转图像并裁剪模板 - 改进版"""
    # 计算旋转角度
    rotation_angle = calculate_rotation_angle(template_corners)
    
    # 计算旋转中心（使用最小外接矩形的中心）
    corners_array = np.array(template_corners, dtype=np.float32)
    rect = cv2.minAreaRect(corners_array)
    center = rect[0]  # 使用最小外接矩形的中心
    
    # 获取旋转矩阵
    rotation_matrix = cv2.getRotationMatrix2D(center, rotation_angle, 1.0)
    
    # 旋转整个图像
    rotated_image = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]))
    
    # 计算旋转后模板的四角坐标
    rotated_corners = [rotate_point(corner, center, rotation_angle) for corner in template_corners]
    
    # 找到旋转后模板的边界框（使用最小外接矩形）
    rotated_corners_array = np.array(rotated_corners, dtype=np.float32)
    rect_rotated = cv2.minAreaRect(rotated_corners_array)
    box_rotated = cv2.boxPoints(rect_rotated)
    box_rotated = np.intp(box_rotated)
    
    # 提取边界框的坐标
    x_coords = box_rotated[:, 0]
    y_coords = box_rotated[:, 1]
    x_min, x_max = np.min(x_coords), np.max(x_coords)
    y_min, y_max = np.min(y_coords), np.max(y_coords)
    
    # 确保边界框在图像范围内
    x_min = max(0, x_min)
    x_max = min(image.shape[1], x_max)
    y_min = max(0, y_min)
    y_max = min(image.shape[0], y_max)
    
    # 计算裁剪后模板的宽度和高度
    template_width = x_max - x_min
    template_height = y_max - y_min
    
    # 确保边界框有效
    if template_width <= 0 or template_height <= 0:
        print(f"警告: 无效的边界框 ({x_min}, {y_min}, {x_max}, {y_max})")
        return None, None, None, None, None, None
    
    # 裁剪模板
    cropped_template = rotated_image[y_min:y_max, x_min:x_max]
    
    # 计算裁剪区域的四角坐标（在旋转后图像中的坐标）
    cropped_corners_rotated = [
        (x_min, y_min),  # 左上
        (x_max, y_min),  # 右上
        (x_max, y_max),  # 右下
        (x_min, y_max)   # 左下
    ]
    
    # 反向旋转裁剪区域的四角坐标，得到在原图中的坐标
    inverse_rotation_matrix = cv2.getRotationMatrix2D(center, -rotation_angle, 1.0)
    
    # 将裁剪区域的四角坐标转换回原图坐标
    original_corners = []
    for corner in cropped_corners_rotated:
        point = np.array([corner[0], corner[1], 1])
        original_point = np.dot(inverse_rotation_matrix, point)
        original_corners.append(tuple(original_point))
    
    # 使用还原后的矩形角点计算中心点
    restored_center_x = np.mean([p[0] for p in original_corners])
    restored_center_y = np.mean([p[1] for p in original_corners])
    restored_center = (restored_center_x, restored_center_y)
    
    return cropped_template, rotation_angle, restored_center, template_width, template_height, original_corners

def process_images_batch(image_dir, label_dir, template_output_dir, output_dir=None):
    """批量处理图像和标签"""
    # 确保输出目录存在
    os.makedirs(template_output_dir, exist_ok=True)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    
    # 创建gt.txt文件
    gt_file_path = os.path.join(template_output_dir, "gt.txt")
    gt_file = open(gt_file_path, "w", encoding="utf-8")
    
    # 获取所有图像文件
    image_extensions = ['*.jpg', '*.jpeg', '*.png', '*.bmp']
    image_files = []
    for ext in image_extensions:
        image_files.extend(glob.glob(os.path.join(image_dir, ext)))
    
    print(f"找到 {len(image_files)} 个图像文件")
    
    # 处理每个图像
    for image_path in image_files:
        print(f"处理图像: {image_path}")
        
        # 读取图像
        image = cv2.imread(image_path)
        if image is None:
            print(f"无法读取图像: {image_path}")
            continue
            
        img_height, img_width = image.shape[:2]
        print(f"图像尺寸: {img_width}x{img_height}")
        
        # 构建对应的标签文件路径
        base_name = os.path.splitext(os.path.basename(image_path))[0]
        label_path = os.path.join(label_dir, base_name + ".txt")
        
        # 检查标签文件是否存在
        if not os.path.exists(label_path):
            print(f"标签文件不存在: {label_path}")
            continue
        
        # 复制图像用于绘制
        image_with_boxes = image.copy()
        
        # 读取标签文件
        with open(label_path, 'r') as f:
            lines = f.readlines()
        
        valid_lines = lines[2:] # 跳过前两行
        print(f"找到 {len(valid_lines)} 个模板")
        
        # 模板计数器
        img_template_count = 0
        
        # 处理每个模板
        for line_idx, line in enumerate(valid_lines):
            parts = line.strip().split()
            if len(parts) < 8:  # 只需要8个坐标值
                print(f"无效的标签行: {line}")
                continue
            
            # 提取坐标
            coords = list(map(float, parts[:8]))
            template_corners = [(coords[i], coords[i+1]) for i in range(0, 8, 2)]
            
            # 处理模板数据
            cropped_template, rotation_angle, center, template_width, template_height, restored_corners = process_template_data(image, template_corners)
            
            if cropped_template is None:
                print(f"模板 {line_idx+1} 处理失败，跳过")
                continue
            
            # 检查模板尺寸是否符合要求 (18-72像素)
            if template_width < 18 or template_width > 72 or template_height < 18 or template_height > 72:
                continue
            
            # 在图像上绘制原始模板框（红色）
            image_with_boxes = draw_polygon(image_with_boxes, template_corners, (0, 0, 255), 2)
            
            # 在图像上绘制还原后的矩形框（绿色）
            image_with_boxes = draw_polygon(image_with_boxes, restored_corners, (0, 255, 0), 2)
            
            # 创建模板文件名
            img_template_count += 1
            template_filename = f"{base_name}_template_{img_template_count:04d}.png"
            template_path = os.path.join(template_output_dir, template_filename)
            
            # 保存模板图像
            if len(cropped_template.shape) == 3 and cropped_template.shape[2] == 3:
                template_rgb = cv2.cvtColor(cropped_template, cv2.COLOR_BGR2RGB)
            else:
                template_rgb = cropped_template
            
            template_pil = Image.fromarray(template_rgb)
            template_pil.save(template_path)
            
            # 写入gt.txt文件
            image_name = os.path.basename(image_path)
            center_x, center_y = center
            
            gt_line = f"{image_name} {template_filename} {center_x:.2f} {center_y:.2f} {template_width/36:.3f} {template_height/36:.3f} {rotation_angle:.2f}\n"
            gt_file.write(gt_line)
        
        # 保存绘制后的图像
        if output_dir and img_template_count!=0 :
            output_path = os.path.join(output_dir, os.path.basename(image_path))
            
            # 将BGR转换为RGB
            if len(image_with_boxes.shape) == 3 and image_with_boxes.shape[2] == 3:
                image_rgb = cv2.cvtColor(image_with_boxes, cv2.COLOR_BGR2RGB)
            else:
                image_rgb = image_with_boxes
            
            output_pil = Image.fromarray(image_rgb)
            output_pil.save(output_path)
            print(f"已保存绘制后的图像: {output_path}")
        
        print("-" * 50)
    
    # 关闭gt.txt文件
    gt_file.close()
    print(f"GT文件已保存: {gt_file_path}")

# 使用示例
if __name__ == "__main__":
    # 设置路径和参数
    image_dir = "/workspace/zhouji/dataSets/DOTA/images/images"  # 替换为你的图像目录
    label_dir = "/workspace/zhouji/dataSets/DOTA/labelTxt" # 替换为你的标签目录
    template_output_dir = "/workspace/zhouji/dataSets/DOTA/templates" # 裁剪模板保存目录
    output_dir = "output_images_with_boxes" # 绘制后的图像保存目录（可选）
    
    # 批量处理
    process_images_batch(image_dir, label_dir, template_output_dir)

````


### data/filterData.py

````python
import csv
from pycocotools.coco import COCO
import math

def filter_data(coco_annotations_path, output_csv_path, tShape=(36, 36), scale_range=(0.5, 2)):
    """
    筛选 COCO 数据集中满足原始 w 和 h 缩放条件的目标（直接基于原始尺寸判断）
      
    参数:
        coco_annotations_path: COCO 数据集的注释文件路径（如 instances_train2017.json）
        output_csv_path: 输出 CSV 文件的路径
        target_shape: 模板的目标尺寸，默认为 (36, 36)
        scale_range: w 和 h 相对于 target_shape 的缩放范围，默认为 (0.5, 2)
    """
    th, tw = tShape
    count = 0
    
    # 加载 COCO 数据集
    coco = COCO(coco_annotations_path)
    img_ids = coco.getImgIds()
    with open(output_csv_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        # csv_writer.writerow(['img_name', 'x', 'y', 'w', 'h'])  # 写入表头
        
        # 遍历所有图像
        for img_id in img_ids:
            # 获取图像信息
            img_info = coco.loadImgs(img_id)[0]
            img_name = img_info['file_name']
            
            # 获取图像对应的标注
            ann_ids = coco.getAnnIds(imgIds=img_id)
            anns = coco.loadAnns(ann_ids)
            
            # 遍历图像中的所有标注
            for ann in anns:
                # 获取边界框
                bbox = ann['bbox']  # [x, y, width, height]
                x, y, w, h = bbox
                x = math.floor(x)
                y = math.floor(y)
                w = math.ceil(w)
                h = math.ceil(h)
                
                # 计算 w 和 h 相对于目标尺寸的缩放比例
                scale_w = w / tw
                scale_h = h / th
                
                # 检查是否满足缩放条件
                if (scale_range[0] <= scale_w <= scale_range[1] and 
                    scale_range[0] <= scale_h <= scale_range[1]):
                    # 需要缩放为1，数据量不够，需进行裁剪
                    # w, h = tw, th
                    # 将满足条件的数据写入 CSV
                    csv_writer.writerow([
                        img_name,
                        x, y, w, h
                    ])
                    count += 1
    print(f"筛选完成，共找到 {count} 个满足条件的目标。")



if __name__ == "__main__":
    # COCO 数据集注释文件路径
    annotations_path = "/path-to/MS-CoCo/annotations/instances_train2017.json"
    
    # 输出 CSV 文件路径
    output_path = 'train.csv'
    
    filter_data(
        annotations_path, 
        output_path, 
        tShape=(36, 36), 
        scale_range=(0.5, 2)
    )

````


### model.py

````python
import torch 
import torch.nn as nn
import torch.nn.functional as F
import timm
from utils import weight_init
     

class convnext_v2_tiny(torch.nn.Module):
    def __init__(self):
        model = timm.create_model('convnextv2_tiny', pretrained=False)
        super().__init__()
        self.stem = model.stem          # Stem层
        self.stage1 = model.stages[0] 
        self.norm = nn.BatchNorm2d(96)
        
    def forward(self, x):
        x = self.stem(x)
        x = self.stage1(x)
        x = self.norm(x)
        return x
    
    def initialize(self):
        for m in self.modules():
            # 仅初始化新增的BatchNorm层（跳过从预训练模型继承的层）
            if isinstance(m, nn.BatchNorm2d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)


class Model(nn.Module):
    def __init__(self, snapshot):
        super(Model, self).__init__()
        self.snapshot       =   snapshot
        self.c              =   96
        self.backbone_T     =   convnext_v2_tiny()
        self.backbone_O     =   convnext_v2_tiny()
        self.pointwise_conv =   nn.Conv2d(in_channels=self.c, out_channels=self.c, kernel_size=3, padding=1)
        self.conv1          =   nn.Conv2d(in_channels=self.c, out_channels=self.c*2, kernel_size=3, padding=1)
        self.conv2          =   nn.Conv2d(in_channels=self.c//2, out_channels=self.c, kernel_size=3, padding=1)
        self.upsample       =   nn.PixelShuffle(2)
        # PixelShuffle: 将每个通道的 4 个像素重新排列到空间维度(无学习权重参数)。从而使通道数减少为原来的 1/4，同时空间维度增加为原来的 2 倍。
        self.conv_score     =   nn.Sequential(
                                    nn.Conv2d(in_channels=self.c//4, out_channels=self.c//8, kernel_size=3, padding=1),
                                    nn.ReLU(),
                                    nn.Conv2d(in_channels=self.c//8, out_channels=1, kernel_size=1, padding=0),
                                    nn.Sigmoid()
                                ) 
        self.conv_sign      =   nn.Sequential(
                                    nn.Conv2d(in_channels=self.c//4, out_channels=self.c//8, kernel_size=3, padding=1),
                                    nn.ReLU(),
                                    nn.Conv2d(in_channels=self.c//8, out_channels=1, kernel_size=1, padding=0),
                                    nn.Sigmoid()
                                )
        self.conv_cos       =   nn.Sequential(
                                    nn.Conv2d(in_channels=self.c//4, out_channels=self.c//8, kernel_size=3, padding=1),
                                    nn.ReLU(),
                                    nn.Conv2d(in_channels=self.c//8, out_channels=1, kernel_size=1, padding=0),
                                    nn.Tanh()
                                )
        self.conv_scale_x   =   nn.Sequential(
                                    nn.Conv2d(in_channels=self.c//4, out_channels=self.c//8, kernel_size=3, padding=1),
                                    nn.ReLU(),
                                    nn.Conv2d(in_channels=self.c//8, out_channels=1, kernel_size=1, padding=0),
                                    nn.Sigmoid()
                                )
        self.conv_scale_y   =   nn.Sequential(
                                    nn.Conv2d(in_channels=self.c//4, out_channels=self.c//8, kernel_size=3, padding=1),
                                    nn.ReLU(),
                                    nn.Conv2d(in_channels=self.c//8, out_channels=1, kernel_size=1, padding=0),
                                    nn.Sigmoid()
                                )
        self.bn1            =   nn.BatchNorm2d(self.c*2)
        self.bn2            =   nn.BatchNorm2d(self.c)

        self.initialize()

    # W = 224, H = 224, K = 16
    # TW = K*4, TH = K*4
    def forward(self, origin, template):
        # search_area: [B, C, H, W] = [B, 3, 224, 224]
        # template: [B, C, H, W] = [B, 3, 16, 16]
        # convnext 的第一个阶段（stage1）会对输入进行 4 倍下采样（shape = [B, self.c, H/4, W/4]）

        # W=H = 56, K = 4
        stage1_o = self.backbone_O(origin)       # (B, self.c, 56, 56)
        stage1_t = self.backbone_T(template)       # (B, self.c, 4, 4)
                        
        # depthiwise + pointwise(backbone_T更新梯度)
        output = []
        b, c, th, tw = stage1_t.shape
        for i in range(b):
            out = F.conv2d(
                    input=stage1_o[i].unsqueeze(0), # [self.c, 1, 56, 56]
                    weight=stage1_t[i].view(c, 1, th, tw), # 显式重塑权重,[self.c, 1, 8, 8]
                    stride=1, padding=(th//2, tw//2),
                    groups=self.c
                    )
            out = self.pointwise_conv(out)
            output.append(out)
        feature = torch.cat(output, dim=0)
        # print("feature: ", feature.shape)
        
        out_conv1 = F.relu(self.bn1(self.conv1(feature)))         # (B, self.c*2, 49, 49) 
        out_subconv1 = self.upsample(out_conv1)                   # (B, self.c//2, 98, 98)                                                                                      
        out_conv2 = F.relu(self.bn2(self.conv2(out_subconv1)))    # (B, self.c, 98, 98)
        out = self.upsample(out_conv2)                            # (B, self.c//4 , 196 , 196)

        score    = self.conv_score(out)       # (B, 1, 196, 196)
        sign     = self.conv_sign(out)
        cos      = self.conv_cos(out)
        scale_x  = self.conv_scale_x(out) * 1.5 + 0.5       # scale: 0.5 ~ 2
        scale_y  = self.conv_scale_y(out) * 1.5 + 0.5       # scale: 0.5 ~ 2
                
        return score, sign, cos, scale_x, scale_y
        

    def initialize(self):
        if self.snapshot:
            print('load model...')
            self.load_state_dict(torch.load(self.snapshot, map_location=torch.device('cpu')))
        else:
            weight_init(self)
            nn.init.kaiming_normal_(self.pointwise_conv.weight, mode='fan_out', nonlinearity='relu')
            nn.init.constant_(self.pointwise_conv.bias, 0)

````


### test.py

````python
import warnings
warnings.filterwarnings("ignore")

import cv2, torch, math, random
from model import Model
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import torchvision.transforms as transforms

from utils import draw_rotated_bbox, get_center
from utils.refine import *
from utils import getIOU


device = torch.device('cpu')

model = Model('dict/model.pth').to(device).eval()

transform_img = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406],  std=[0.229, 0.224, 0.225]),
        ])
        
def denormalize(tensor, mean=[0.485, 0.456, 0.406], std = [0.229, 0.224, 0.225]):
    mean = torch.tensor(mean).view(3, 1, 1)
    std = torch.tensor(std).view(3, 1, 1)
    return tensor * std + mean


query_image_path = './res/image.png'
template_image_path = './res/template.png'
with torch.no_grad():
    image = cv2.imread(query_image_path)
    template = cv2.imread(template_image_path)
    template = cv2.resize(template, (36, 36))
    
    image = transform_img(Image.fromarray(image)).to(device).unsqueeze(0)
    template = transform_img(Image.fromarray(template)).to(device).unsqueeze(0)
        
    pred_score, pred_sign, pred_cos, pred_scale_x, pred_scale_y = model(image, template)
    
    # 计算 center
    pred = pred_score[0, 0, :, :]
    max_idx = torch.nonzero(pred == pred.max())[0]
    pre_Y, pre_X = max_idx.cpu().numpy()
    pred_y, pred_x = get_center((pre_Y, pre_X), torch.nonzero(pred > 0.5).cpu().numpy())
    
    # 计算 角度
    sign = 1 if pred_sign[0, 0, pre_Y, pre_X] > 0.5 else -1
    pred_r = torch.arccos(pred_cos[0, 0, pre_Y, pre_X].clamp(-1, 1)) * 180 / math.pi
    pred_r = sign * pred_r.item()
    
    # 计算缩放
    pred_sx = pred_scale_x[0, 0, pre_Y, pre_X].item()
    pred_sy = pred_scale_y[0, 0, pre_Y, pre_X].item()
    
    search_img = (denormalize(image.squeeze(0))).permute(1, 2, 0).cpu().numpy()
    template_img = (denormalize(template.squeeze(0))).permute(1, 2, 0).cpu().numpy()
    
    # 细化
    pred_r, _ = refine_angle_bisection(
        search_img, template_img, pred_x, pred_y, pred_sx, pred_sy, pred_r,
        initial_range=20,
    )
    pred_sx, _ = refine_scale_x(
        search_img, template_img, pred_x, pred_y, pred_sx, pred_sy, pred_r
    )
    pred_sy, _ = refine_scale_y(
        search_img, template_img, pred_x, pred_y, pred_sx, pred_sy, pred_r
    )
    pred_r, _ = refine_angle(
        search_img, template_img, pred_x, pred_y, pred_sx, pred_sy, pred_r,
        initial_range=5
    )
    
    # 计算IOU
    pred_param = np.array([pred_x, pred_y, pred_sx, pred_sy, pred_r], dtype=np.float32)
    true_param = np.array([45,95,0.89,0.90,-50], dtype=np.float32)
    IoU = getIOU(true_param, pred_param, 36, 36)
    
    fig, ax = plt.subplots(figsize=(2.24, 2.24), dpi=300)
    ax.imshow(search_img[..., ::-1]) # BGR->RGB 
    draw_rotated_bbox(ax, pred_param, 'green', 36, 36)
    # draw_rotated_bbox(ax, true_param, 'red', 36, 36)

    ax.axis('off')
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    plt.savefig('res/res.jpg', bbox_inches='tight', pad_inches=0)
    
    print('\t\tcenter\t\t\tscale_x\t\t\tscale_y\t\t\tangle\t\t\tIOU')

    print(f'true:\t\t{true_param[0]:<6.2f} {true_param[1]:<6.2f}', end='\t\t')
    print(f'{true_param[2]:.2f}',end='\t\t\t')
    print(f'{true_param[3]:.2f}', end='\t\t\t')
    print(f'{true_param[4]:.2f}', end='\t\t\t')
    print(1)

    print(f'pre:\t\t{pred_x:<6.2f} {pred_y:<6.2f}', end='\t\t')
    print(f'{pred_sx:.2f}',end='\t\t\t')
    print(f'{pred_sy:.2f}', end='\t\t\t')
    print(f'{pred_r:.2f}', end='\t\t\t')
    print(f'{IoU:.2f}')

````


### test_single.py

````python
import warnings
warnings.filterwarnings("ignore")

import cv2, torch, math, time
import numpy as np
from model import Model
from utils import CoCo_Dataset, get_center, getIOU
from utils.refine import *

import random
random.seed(42)
np.random.seed(42)
torch.manual_seed(42)
torch.cuda.manual_seed(42)


th, tw = 36, 36
rootPath = '/workspace/zhouji/dataSets/MS-CoCo/val2017/'
test_file = 'data/S2/val.csv'
model_file ='dict/model.pth'
result_file = 'res/result-tiny.txt'
device = torch.device('cpu')

model = Model(None).to(device)
state_dict = torch.load(model_file, map_location=device)
model.load_state_dict(state_dict)
model.eval()

dataset = CoCo_Dataset(rootPath, test_file, (th, tw))

success_count = 0
max_samples = 1000

locErr, angleErr, scaleXErr, scaleYErr, mIoU = 0.0, 0.0, 0.0, 0.0, 0.0
all_time = 0.0

with open(result_file, 'w', encoding='utf-8') as rf:
    rf.write('===== 批量模板匹配结果 =====\n\n')

    with torch.no_grad():
        for i in range(min(len(dataset), max_samples)):
            print("Processing sample:", i + 1)
            name, image, template, true_y, true_x, true_sy, true_sx, true_r = dataset[i]
            image = image.unsqueeze(0).to(device)
            template = template.unsqueeze(0).to(device)
            
            start_time = time.time()
            pred_score, pred_sign, pred_cos, pred_scale_x, pred_scale_y = model(image, template)
            inference_time = time.time() - start_time

            pred = pred_score[0, 0, :, :]
            max_idx = torch.nonzero(pred == pred.max())[0]
            pre_Y, pre_X = max_idx.cpu().numpy()
            pred_y, pred_x = get_center((pre_Y, pre_X), torch.nonzero(pred > 0.5).cpu().numpy())

            gt_param = np.array([true_x, true_y, true_sx, true_sy, true_r], dtype=np.float32)

            # 计算预测参数
            sign = 1 if pred_sign[0, 0, pre_Y, pre_X] > 0.5 else -1
            pred_r = torch.arccos(pred_cos[0, 0, pre_Y, pre_X].clamp(-1, 1)) * 180 / math.pi
            pred_r = sign * pred_r.item()
            
            # 计算缩放
            pred_sx = pred_scale_x[0, 0, pre_Y, pre_X].item()
            pred_sy = pred_scale_y[0, 0, pre_Y, pre_X].item()
            pred_param = np.array([pred_x, pred_y, pred_sx, pred_sy, pred_r], dtype=np.float32)

            search_img = ((image.squeeze(0) * 0.5 + 0.5)).permute(1, 2, 0).cpu().numpy()
            template_img = ((template.squeeze(0)*0.5+0.5)).permute(1, 2, 0).cpu().numpy()
            
            search_img = cv2.cvtColor(search_img, cv2.COLOR_BGR2GRAY)
            template_img = cv2.cvtColor(template_img, cv2.COLOR_BGR2GRAY)
            
            # 进行角度细化
            post_start = time.time()
            refined_angle, refine_score = refine_angle_bisection(
                search_img, template_img, pred_x, pred_y, pred_sx, pred_sy, pred_r,
            )
            pred_sx, _ = refine_scale_x(
                search_img, template_img, pred_x, pred_y, pred_sx, pred_sy, refined_angle,
                search_range=0.15, step_size=0.015
            )
            pred_sy, _ = refine_scale_y(
                search_img, template_img, pred_x, pred_y, pred_sx, pred_sy, refined_angle,
                search_range=0.15, step_size=0.015
            )
            post_time = time.time() - post_start

            pos_error = np.sqrt((pred_x - true_x) ** 2 + (pred_y - true_y) ** 2)
            angle_error = abs(pred_r - true_r)
            refined_angle_error = abs(refined_angle - true_r)
            angle_error = min(angle_error, 360 - angle_error)
            refined_angle_error = min(refined_angle_error, abs(360 - refined_angle_error))
            scale_x_error = abs(pred_sx - true_sx)
            scale_y_error = abs(pred_sy - true_sy)
            
            # 计算IOU
            pred_param = np.array([pred_x, pred_y, pred_sx, pred_sy, refined_angle], dtype=np.float32)
            IOU = getIOU(pred_param, gt_param, th, tw)

            match_success = (pred_score[0, 0, pre_Y, pre_X].item() > 0.01 and IOU > 0.1)
            if match_success:
                success_count += 1
                rf.write(f'样本 {i} -- {name} \n')
                rf.write('状态: 匹配成功(GT vs. Pred)\n')
                rf.write(f'center: ({true_x:.2f},{true_y:.2f}) vs ({pred_x:.2f},{pred_y:.2f}) 误差: {pos_error:.2f}\n')
                rf.write(f'angle: {true_r:.2f}° vs {refined_angle:.2f}° 误差: {refined_angle_error:.2f}°\n')
                rf.write(f'scale_x: {true_sx:.3f} vs {pred_sx:.3f} 误差: {scale_x_error:.3f}\n')
                rf.write(f'scale_y: {true_sy:.3f} vs {pred_sy:.3f} 误差: {scale_y_error:.3f}\n')
                rf.write(f'IOU: {IOU:.3f}\n')
                rf.write(f'Time(ms): {inference_time*1000:.1f} + {post_time*1000:.1f}')
                rf.write(f'={(inference_time+post_time)*1000:.1f}\n')
                
                locErr += pos_error
                angleErr += refined_angle_error
                scaleXErr += scale_x_error
                scaleYErr += scale_y_error
                mIoU += IOU
                all_time += (inference_time + post_time)   
            else:
                rf.write(f'样本 {i}:\n')
                rf.write('状态: 匹配失败\n')
 
            rf.write('----------------------------\n\n')
            
    rf.write('===== 批量模板匹配结果统计 =====\n\n')
    rf.write(f'总样本数: {min(len(dataset), max_samples)}\n')
    rf.write(f'匹配成功样本数: {success_count}\n')
    rf.write(f'匹配成功率: {success_count / min(len(dataset), max_samples) * 100:.2f}%\n')
    if success_count > 0:
        rf.write(f'平均位置误差: {locErr / success_count:.2f}像素\n')
        rf.write(f'平均角度误差: {angleErr / success_count:.2f}°\n')
        rf.write(f'平均缩放X误差: {scaleXErr / success_count:.3f}\n')
        rf.write(f'平均缩放Y误差: {scaleYErr / success_count:.3f}\n')
        rf.write(f'平均IOU: {mIoU / success_count:.3f}\n')
        rf.write(f'平均时间: {all_time / 1000 * min(len(dataset), max_samples):.2f} ms\n')
    else:
        rf.write('没有成功匹配的样本，无法计算平均误差。\n')

````


### train.py

````python
import warnings
warnings.filterwarnings("ignore")

import os, time
os.environ["CUDA_VISIBLE_DEVICES"] = '0'
import argparse, torch, math
from model import Model
from pathlib import Path  
from torch.utils.data import DataLoader 
import torch.optim as optim
from utils import create_gt
from utils import CoCo_Dataset
from utils import reg_loss, soft_focal_loss, Sign_Loss


def get_args_parser():
    parser = argparse.ArgumentParser('Set detector', add_help=False)
    
    parser.add_argument('--batch_size', default=64, type=int)
    parser.add_argument('--lr', default=1e-3, type=float)
    parser.add_argument('--th', default=36, type=int)
    parser.add_argument('--tw', default=36, type=int)
    
    parser.add_argument('--train_imgPath',  default='/workspace/zhouji/dataSets/MS-CoCo/train2017/')
    parser.add_argument('--val_imgPath',    default='/workspace/zhouji/dataSets/MS-CoCo/val2017/')
    parser.add_argument('--train_file',     default='data/S2/train.csv')
    parser.add_argument('--val_file',       default='data/S2/val.csv')
    parser.add_argument('--snapshot',       default=None)
    # parser.add_argument('--snapshot',       default="./dict/model_epoch_200.pth")

    parser.add_argument('--device',         default='cuda')
    parser.add_argument('--start_epoch',    default=0,   type=int)
    parser.add_argument('--epochs',         default=200, type=int)
    parser.add_argument('--save_interval',  default=25,  type=int)
    parser.add_argument('--val_interval',   default=25,  type=int)
    
    parser.add_argument('--losslog',        default='./dict/log/log.txt')
    parser.add_argument('--output_dir',     default='./dict/', help='path to save model')
    return parser

def TemplatMacthLoss(pred_score, gt_score, pred_sign, pred_cos, pred_scale_x, pred_scale_y, gt_param):  
    mask        = (gt_score != 0).float()
    
    scoreLoss   = soft_focal_loss(pred_score[:, 0, :, :], gt_score)
    signLoss, acc = Sign_Loss(pred_sign[:, 0, :, :], gt_param[:, 0, :, :], mask)
    cosLoss = reg_loss(pred_cos[:, 0, :, :], gt_param[:, 1, :, :], mask)
    
    diff, b = 0, gt_score.shape[0]
    for i in range(b):
        gt_y, gt_x = torch.nonzero(gt_score[i, :, :] == gt_score[i, :, :].max())[0]
        pred_angle = torch.arccos(pred_cos[i, 0, gt_y, gt_x])
        gt_angle   = torch.arccos(gt_param[i, 1, gt_y, gt_x])
        diff += torch.abs(pred_angle - gt_angle) * 180 / math.pi
    diff /= b
    
    scaleLoss_x = reg_loss(pred_scale_x[:, 0, :, :], gt_param[:, 2, :, :], mask)
    scaleLoss_y = reg_loss(pred_scale_y[:, 0, :, :], gt_param[:, 3, :, :], mask)
    
    total_loss = scoreLoss + signLoss + cosLoss + scaleLoss_x + scaleLoss_y
    
    return  total_loss, scoreLoss, signLoss, cosLoss, scaleLoss_x, scaleLoss_y, acc, diff

def val(model, val_loader, device, template_shape):
    model.eval()
    acccuray, anglediff = 0.0, 0.0
    with torch.no_grad():
        for i, (_,images, bboxes, center_y, center_x, scale_y, scale_x, angle) in enumerate(val_loader):
            images = images.to(device, non_blocking=True).float()
            bboxes = bboxes.to(device, non_blocking=True).float()
            torch.cuda.empty_cache()
            
            true_params = torch.stack([center_y, center_x, scale_y, scale_x, angle], dim=1).to(torch.float32)
            
            # sign, cos, scale_x, scale_y
            gt_score, gt_param = create_gt(images, true_params, template_shape)
            gt_param, gt_score = gt_param.to(device), gt_score.to(device)
            
            pred_score, pred_sign, pred_cos, pred_scale_x, pred_scale_y = model(images, bboxes)
            *_, acc, diff = TemplatMacthLoss(pred_score, gt_score, pred_sign, pred_cos, pred_scale_x, pred_scale_y, gt_param)
            
            # 计算准确率
            acccuray   += acc.item()
            anglediff  += diff.item()
            
            if i == 200: break
        
        acccuray /= min((i+1), len(val_loader)); anglediff /= min((i+1), len(val_loader))
        return acccuray, anglediff
        
def train(model, train_loader, optimizer, device, template_shape):
    model.train()
    total_loss, scoreloss, signloss, cosloss, scaleloss_x, scaleloss_y = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
    acccuray, anglediff = 0.0, 0.0
    for i, (_,images, bboxes, center_y, center_x, scale_y, scale_x, angle) in enumerate(train_loader):
        images = images.to(device, non_blocking=True).float()
        bboxes = bboxes.to(device, non_blocking=True).float()
        torch.cuda.empty_cache()
        
        true_params = torch.stack([center_y, center_x, scale_y, scale_x, angle], dim=1).to(torch.float32)
        
        # sign, cos, sx, sy
        gt_score, gt_param = create_gt(images, true_params, template_shape)
        gt_param, gt_score = gt_param.to(device), gt_score.to(device)

        optimizer.zero_grad(set_to_none=True) 
        
        pred_score, pred_sign, pred_cos, pred_scale_x, pred_scale_y = model(images, bboxes)

        loss, scoreLoss, signLoss, cosLoss, scaleLoss_x, scaleLoss_y, acc, diff = \
            TemplatMacthLoss(pred_score, gt_score, pred_sign, pred_cos, pred_scale_x, pred_scale_y, gt_param)
        
        loss.backward()
        optimizer.step()
        
        total_loss  += loss.item()
        scoreloss   += scoreLoss.item()
        signloss    += signLoss.item()
        cosloss     += cosLoss.item()
        scaleloss_x += scaleLoss_x.item()
        scaleloss_y += scaleLoss_y.item()
        acccuray    += acc.item()
        anglediff   += diff.item()
        
        if i >= 1000: break

    All_loss = [total_loss, scoreloss, signloss, cosloss, scaleloss_x, scaleloss_y, acccuray, anglediff]
    return [x / min((i+1), len(train_loader)) for x in All_loss]


def main(args):
    if not args.output_dir:
        os.makedirs(args.output_dir)

    device = torch.device(args.device)
    model = Model(args.snapshot).to(device)
    optimizer = optim.Adam(model.parameters(), lr=args.lr)
    
    template_shape = (args.th, args.tw)
    
    train_dataset = CoCo_Dataset(args.train_imgPath, args.train_file, template_shape)
    train_loader = DataLoader(train_dataset, batch_size=args.batch_size, shuffle=True)
    val_dataset = CoCo_Dataset(args.val_imgPath, args.val_file, template_shape)
    val_loader = DataLoader(val_dataset, batch_size=args.batch_size, shuffle=False)
    
    print(f"模板形状  :{template_shape}")
    print(f"训练数据集: {len(train_dataset)}")
    print(f"验证数据集: {len(val_dataset)}")
    
    for epoch in range(args.start_epoch, args.epochs):
        if (epoch + 1) % args.save_interval == 0:
            torch.save(model.state_dict(), args.output_dir + f'model_epoch_{epoch+1}.pth')
        
        if (epoch+1) % args.val_interval == 0:
            try:
                accuray, angle = val(model, val_loader, device, template_shape)
                with open(args.losslog, 'a') as f:
                    f.write(f'Val Epoch [{epoch+1}/{args.epochs}], '
                            f'Acc: {accuray*100:.2f}%, '
                            f'Angle: {angle:.4f},\n'
                            )
            except:
                ...
                        
        loss, scoreLoss, signLoss, cosLoss, scaleLoss_x, scaleLoss_y, accuray, angle = \
            train(model, train_loader, optimizer, device, template_shape)

        with open(args.losslog, 'a') as f:
            f.write(f'Train Epoch [{epoch+1}/{args.epochs}], '
                        f'all: {loss:.4f}, '
                        f'score: {scoreLoss:.4f}, '
                        f'sign: {signLoss:.4f}, '
                        f'cos: {cosLoss:.4f}, '
                        f'scale_x: {scaleLoss_x:.4f}, '
                        f'scale_y: {scaleLoss_y:.4f}, '
                        f'Acc: {accuray*100:.2f}, '
                        f'angle: {angle:.4f},\n'
                        )

if __name__ == '__main__':
    parser = argparse.ArgumentParser('training script', parents=[get_args_parser()])
    args = parser.parse_args()
    if args.output_dir:
        Path(args.output_dir).mkdir(parents=True, exist_ok=True)
    main(args)

````


### utils/__init__.py

````python
# for train
from .tools import weight_init, gaussian2D, create_gt

# for test
from .tool import get_center, draw_rotated_bbox, rotated_rect, getIOU


from .dataSet import CoCo_Dataset


from .loss import soft_focal_loss, reg_loss, Sign_Loss

# 生成训练数据图像对的关键代码
from .get_imgR import rotate_crop


from .refine import refine_angle_bisection, refine_scale_x, refine_scale_y, refine_position, refine_angle

````


### utils/dataSet.py

````python
import torchvision.transforms as transforms
import cv2, json, torch, random, csv, os
from torch.utils.data import Dataset
from PIL import Image
import numpy as np
from .get_imgR import rotate_crop
import pandas as pd
    

class CoCo_Dataset(Dataset):
    def __init__(self, imgPath, fileName, tShape):
        self.transform_img = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[0.485, 0.456, 0.406],  
                std=[0.229, 0.224, 0.225]
            )            
        ])
        self.transform_roi = transforms.Compose([
            transforms.Resize(tShape),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[0.485, 0.456, 0.406],  
                std=[0.229, 0.224, 0.225]
            )            
        ])
        self.imgPath   = imgPath
        self.samples   = []
        self.tShape    = tShape
        
        with open(fileName, 'r') as lines:
            for line in lines:
                name, x, y, w, h = line.strip().split(',')
                self.samples.append([
                    name,
                    (int(x), int(y), int(w), int(h))
                ])
    
    def __len__(self):
        return len(self.samples)
    
    # 数据操作
    def __getitem__(self, idx):
        while True:
            name, bbox  = self.samples[idx]
            image       = cv2.imread(self.imgPath + name)
            image       = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            
            x, y, w, h =  [round(v) for v in bbox]
            template   =  image[y:y+h, x:x+w]
             
            # rotate_crop Image
            imgR, corners, angle = rotate_crop(image, bbox)
            if imgR is None:
                idx = random.randint(0, len(self.samples)-1)
                continue

            scale_y    =  h / self.tShape[0]
            scale_x    =  w / self.tShape[1]
            center     = corners.mean(axis=0)  # 计算中心点

            imgR       = self.transform_img(Image.fromarray(imgR))
            template   = self.transform_roi(Image.fromarray(template))
            
            return name, imgR, template, center[1], center[0], scale_y, scale_x, angle

````


### utils/get_imgR.py

````python
# 生成带有旋转角度的目标框算法：

# 步骤一. 随机角度旋转带有目标框(bbox)图像 --- 得到imgR, bboxR
# 步骤二. 由于旋转后四个角落会产生空白，需要进行裁剪
   # 裁剪要求：不能含有空白部分，包含完整的边界框，剪切后图像大于size：224*224
   # 裁剪算法：
	# 计算目标框bboxR的最小外接矩形，
	# 1）外接矩形已经有部分超出imgR，即与空白部分有相交，回到步骤一（最多10次尝试）
	# 2）仍然在imgR中，则开始扩大剪切区域，计算每条边S可以扩张的距离maxD_S(受size和目标框bboxR限制)
	   # 即：移动后S与imgR边界的两个交点距离需等于224 (可移动距离为含有0，回到步骤一)
	   # a. 随机选择一条边s向外扩张（移动），移动距离为计算出的最大范围内随机【0，maxD_s】, 同时确认出对边的位置
	   # b. 移动后需要更新其邻边的最大移动距离
		# -- 相邻的两条边的最大扩张距离受到S与imgR产生的两个新交点
		# -- 更新可移动距离含有0，回到步骤a
	   # c. 在剩余的邻边里随机选择一边重复步骤ab
	   # d. 剪切扩张后的矩形

import numpy as np
import cv2, copy, math
import matplotlib.pyplot as plt


def rotate_crop(image, bbox, max_attempts: int = 10):
    for i in range(max_attempts):
        # 步骤一：随机旋转图像和边界框
        angle = np.random.uniform(-180, 180)  # 随机旋转角度，可调整范围
        img_R, bbox_R = rotate(image, bbox, angle)

        # 计算旋转后边界框的最小外接矩形
        min_rect = get_min_rect(bbox_R)
        rect = min_rect.copy()
        
        # 检查边界框是否与空白区域相交
        if rect_in_imgR(rect, img_R):
            # 步骤二：扩张裁剪区域
            crop_rect = expand_rect(rect, img_R, angle, size=224)
            if crop_rect is not None and  rect_in_imgR(crop_rect, img_R):
                # 裁剪图像
                x, y, w, h = crop_rect
                cropped_img = img_R[y:y+224, x:x+224]
                # 更新边界框坐标到裁剪后的坐标系
                bbox_R[:, 0] -= x
                bbox_R[:, 1] -= y
                return cropped_img, bbox_R, angle
    
    # 如果所有尝试都失败，返回None
    return None, None, None


def rotate(image, bbox, angle):
    """
    旋转图像和边界框，确保旋转后的图像包含所有原始内容
    
    Args:
        image: 原始图像
        bbox: 边界框 [x, y, w, h]
        angle: 旋转角度（角度制）
    
    Returns:
        rotated_img: 旋转后的图像
        rotated_bbox: 旋转后的边界框顶点坐标（相对于新图像）
    """
    h, w = image.shape[:2]
    
    # 计算旋转后需要的图像大小
    corners = np.array([
        [0, 0],
        [w-1, 0],
        [w-1, h-1],
        [0, h-1]
    ], dtype=np.float32)
    
    # 转换角度为弧度
    angle_rad = np.deg2rad(angle)
    
    # 计算旋转中心（图像中心）
    cx, cy = w / 2, h / 2
    
    # 旋转后的角点
    rotated_corners = []
    for x, y in corners:
        # 平移到原点
        x -= cx
        y -= cy
        
        # 旋转
        x_rot = x * np.cos(angle_rad) - y * np.sin(angle_rad)
        y_rot = x * np.sin(angle_rad) + y * np.cos(angle_rad)
        
        # 平移回来
        x_rot += cx
        y_rot += cy
        
        rotated_corners.append([x_rot, y_rot])
    
    rotated_corners = np.array(rotated_corners)
    
    # 计算旋转后的边界
    x_min = np.floor(np.min(rotated_corners[:, 0]))
    y_min = np.floor(np.min(rotated_corners[:, 1]))
    x_max = np.ceil(np.max(rotated_corners[:, 0]))
    y_max = np.ceil(np.max(rotated_corners[:, 1]))
    
    # 计算新图像的大小
    new_width = int(x_max - x_min)
    new_height = int(y_max - y_min)
    
    # 创建新的转换矩阵，考虑平移
    M = cv2.getRotationMatrix2D((cx, cy), angle, 1.0)
    
    # 添加平移，以确保所有内容都在新图像中
    M[0, 2] += -x_min
    M[1, 2] += -y_min
    
    # 执行仿射变换
    rotated_img = cv2.warpAffine(image, M, (new_width, new_height), flags=cv2.INTER_LINEAR)
    
    # 旋转边界框
    # x, y, width, height = bbox
    x, y, width, height = [round(val) for val in bbox]  # 确保是整数
    bbox_corners = np.array([
        [x, y],
        [x + width, y],
        [x + width, y + height],
        [x, y + height]
    ])
    
    # 转换为齐次坐标
    bbox_corners_h = np.hstack((bbox_corners, np.ones((4, 1))))
    
    # 应用旋转加平移变换
    rotated_bbox_corners = np.dot(M, bbox_corners_h.T).T
    
    return rotated_img, rotated_bbox_corners


def get_min_rect(points):
    """
    计算点集的最小外接矩形
    """
    rect = cv2.minAreaRect(points.astype(np.float32))
    box = cv2.boxPoints(rect)
    box = np.array(box, dtype=np.intp)  # 使用 np.intp 替代 np.int0
    
    # 获取矩形的左上角和右下角坐标
    x_min = np.min(box[:, 0])
    y_min = np.min(box[:, 1])
    x_max = np.max(box[:, 0])
    y_max = np.max(box[:, 1])
    
    return [x_min, y_min, x_max - x_min, y_max - y_min]


def rect_in_imgR(rect, image) -> bool:
    x, y, w, h = rect
    H, W, c = image.shape
    
    # 检查四个角的像素是否为空白
    corners = [
        (x, y),
        (x + w - 1, y),
        (x + w - 1, y + h - 1),
        (x, y + h - 1)
    ]
    for cx, cy in corners:
        if cx < 0 or cy < 0 or cx >= W or cy >= H:
            return False
        if np.all(image[cy, cx] == 0): 
            return False
    
    return True


def expand_rect(rect, image, angle, size=224):
    """
    在满足约束条件的情况下扩张矩形
    
    Args:
        rect: 初始矩形 [x, y, w, h]
        image: 图像
        size: 最小尺寸要求
    
    Returns:
        rect: 扩张后的矩形, 如果无法满足条件则返回None
    """
    h, w = image.shape[:2]
    rect_try = copy.deepcopy(rect)
    
    min_d, max_d = get_expand_range(rect_try, 'left', (h, w), angle, size)
    if max_d < min_d or max_d < 0:
        return None

    # 随机选择扩张距离
    expansion = np.random.uniform(min_d, max_d)  
    rect_try[0] -= expansion
    
    min_d, max_d = get_expand_range(rect_try, 'top', (h, w), angle, size)
    if max_d < min_d or max_d < 0:
        return None

    expansion = np.random.uniform(min_d, max_d)  
    rect_try[1] -= expansion
        
        
    # 成功
    rect_try[0] = math.floor(rect_try[0])
    rect_try[1] = math.floor(rect_try[1])
    rect_try[2] = size
    rect_try[3] = size
    return rect_try 


def get_expand_range(rect, edge, shape, angle, size: int=224) -> tuple:
    H, W = shape
    x, y, w, h = rect
    angle = (angle+180) % 90
    
    # 将角度转换为弧度
    angle_rad = np.deg2rad(angle)
    sin = np.sin(angle_rad)
    cos = np.cos(angle_rad)
    tan = sin / cos
    
    if W < size or H < size: return (-1, -1)
    # 边S与图像边的交点距离公式为: dist = D / (sin_angle * cos_angle)
    # 其中D是边S与图像边界的垂直距离，D与大（向中间靠拢）dis也会逐渐增大
    # 需要保证 dist >= size
    # 所以 D = size * sin_angle * cos_angle
    D = size * sin * cos
    if H < 2*D + size or W < 2*D + size: return(-1, -1)
    
    # 考虑有没有包含边界框
    
    # [0-90] --- 其它角度都可以转到【0-90】来处理
    # 计算rect与imgR左边交点情况（左边）
    #   1. 两个交点位于imgR左上边：只考虑rect上交点
    #   2. rect上交点位于imgR左上边，rect下交点位于imgR左下边：都考虑
    #   3. 两个交点位于imgR左下边：只考虑rect下交点
    
    # 左边
    if edge == 'left':
        cor = W * sin  # imgR左边角点位于image上的 y坐标
        if y < cor and (y+h) < cor : # 情况1
            DL  = (cor-y) / tan
            
        elif y < cor and (y+h) > cor : # 情况2
            DL1 = (cor-y) / tan
            DL2 = (y+h-cor) * tan
            DL  = max(DL1, DL2)
            
        else: # y > cor and (y+h) > cor : # 情况3
            DL  = (y+h-cor) * tan
            
        max_d = min(x - max(DL, D), size-w)
        # 保证右边
        min_d = max(x + size + D - W, 0)
        
        return (min_d, max_d)
            
    # 上边
    elif edge == 'top':
        cor = W * cos  # imgR上边角点位于image上的 x坐标
        if x < cor and (x+w) < cor : # 情况1
            DL  = (cor-x) * tan
            
        if x < cor and (x+w) > cor : # 情况2
            DL1 = (cor-x) * tan
            DL2 = (x+w-cor) / tan
            DL  = max(DL1, DL2)
            
        if x > cor and (x+w) > cor : # 情况3
            DL  = (x+w-cor) / tan
            
        max_d = min(y - max(DL, D), size-h)
        
        # 保证下边
        min_d = max(y + size + D - H, 0)
        
        return (min_d, max_d)  

````


### utils/loss.py

````python
import torch
import torch.nn.functional as F

def soft_focal_loss(pred, gt_score, alpha=2.0, beta=4.0):
    pred = torch.clamp(pred, 1e-6, 1.0 - 1e-6) # 限制预测值，防止出现梯度消失/爆炸
    
    pos_inds = gt_score.ge(0.5).float() # 大于等于0.5 设为正样本 设置为一个二值化掩码
    neg_inds  = gt_score.lt(0.5).float() # 小于0.5设为负样本
    
    neg_weights = torch.pow(1 - gt_score, beta)# 背景权重
    loss = 0
    # 正样本损失
    pos_loss = torch.log(pred) * torch.pow(gt_score - pred, alpha) * pos_inds
    # 负样本损失
    neg_loss = torch.log(1 - pred) * torch.pow(pred, alpha) * neg_weights * neg_inds
    
    num_pos = pos_inds.float().sum() # 正样本个数
    pos_loss = pos_loss.sum()
    neg_loss = neg_loss.sum()
    
    if num_pos == 0:
        loss = loss - neg_loss
    else:
        loss = loss - (pos_loss + neg_loss) / num_pos
    return loss

def center_loss(pred, gt):
    # 限制预测值，防止出现梯度消失/爆炸
    pred = torch.clamp(pred, 1e-6, 1.0 - 1e-6) 
    
    pos_mask = gt.ge(0.5).float() # 大于等于0.5 设为正样本 设置为一个二值化掩码
    neg_mask  = gt.lt(0.5).float() # 小于0.5设为负样本
    
    # 正样本损失
    # pos_loss = F.binary_cross_entropy(pred, gt, reduction="none") * pos_mask
    pos_loss = (gt * torch.log(pred) + (1-gt) * torch.log(1-pred)) * pos_mask
    # 负样本损失 --- mask(1-gt) 全是1
    neg_loss = torch.log(1 - pred) * neg_mask
    
    num_pos = pos_mask.sum().clamp(min=1.0) # 正样本个数
    
    loss = - (pos_loss.sum() + neg_loss.sum()) / num_pos
    return loss


def reg_loss(pred, gt_param, mask):
    regr_loss = F.smooth_l1_loss(pred * mask, gt_param * mask, reduction='sum')
    regr_loss = regr_loss / (mask.sum() + 1e-6)

    return regr_loss 


def Sign_Loss(pred, gt_param, mask):
    acc = ((pred.round() == gt_param)* mask).sum() / (mask.sum() + 1e-6)  # 正确率
    pos_weight = (gt_param * mask).sum() / (mask.sum() + 1e-6)
    neg_weight = 1 - pos_weight
    sign_loss = F.binary_cross_entropy_with_logits(pred * mask, gt_param * mask, reduction='none') 
    # reduction='none'：保持原始形状，不进行均值或求和，以便后续加权。
    
    weighted_loss = sign_loss * (gt_param * pos_weight + (1-gt_param) * neg_weight)
    sign_loss = (weighted_loss * mask).sum() / (mask.sum() + 1e-6) 

    # `Sign_Loss` 的目的是衡量预测值 `pred` 与真实标签 `gt_param` 在符号（正负）上的匹配程度，
    # 最终 `loss` 反映的是模型在符号预测上的误差。
    return sign_loss, acc


````


### utils/refine.py

````python
import cv2, math
import numpy as np


def rotate_template(template, angle, scale_x, scale_y):
    """旋转缩放模板，避免裁剪（warp 输出大小扩展为 sqrt(2)）"""
    th, tw = template.shape[:2]

    # 缩放尺寸
    scaled_th = int(th * scale_y)
    scaled_tw = int(tw * scale_x)
    scaled_template = cv2.resize(template, (scaled_tw, scaled_th))
    mask = np.ones((scaled_th, scaled_tw), dtype=np.uint8)

    # 计算放大后的安全边界尺寸（对角包围盒）
    diagonal_ratio = math.sqrt(2)
    safe_h = int(scaled_th * diagonal_ratio)
    safe_w = int(scaled_tw * diagonal_ratio)

    # 保证尺寸为偶数，便于后续中心对齐等操作
    safe_h += safe_h % 2
    safe_w += safe_w % 2

    # 新中心
    new_center = (safe_w // 2, safe_h // 2)

    # 计算仿射矩阵：从缩放后的模板中心 -> 新中心
    old_center = (scaled_tw // 2, scaled_th // 2)
    M = cv2.getRotationMatrix2D(old_center, angle, 1.0)
    M[0, 2] += new_center[0] - old_center[0]
    M[1, 2] += new_center[1] - old_center[1]

    rotated_template = cv2.warpAffine(scaled_template, M, (safe_w, safe_h), borderValue=0)
    rotated_mask = cv2.warpAffine(mask, M, (safe_w, safe_h), borderValue=0)

    return rotated_mask, rotated_template


def extract_subpixel_patch(image, cx, cy, patch_w, patch_h):
    """从 image 中提取以 (cx, cy) 为中心的 patch，支持亚像素精度"""
    dst_center = (patch_w / 2, patch_h / 2)

    # 构造平移矩阵，把目标点平移到中心
    dx = dst_center[0] - cx
    dy = dst_center[1] - cy
    M = np.array([[1, 0, dx],
                  [0, 1, dy]], dtype=np.float32)

    patch = cv2.warpAffine(image, M, (patch_w, patch_h), flags=cv2.INTER_LINEAR, borderValue=0)
    return patch


def compute_masked_similarity(search_img, rotated_template, mask, cx, cy):
    """仅在模板对应区域中进行相似度计算"""
    
    patch = extract_subpixel_patch(search_img, cx, cy, rotated_template.shape[1], rotated_template.shape[0])

    if len(patch.shape) == 3:
        masked_patch = patch * mask[..., np.newaxis]
        patch_pixels = masked_patch[mask > 0].flatten().astype(np.float32)
        template_pixels = rotated_template[mask > 0].flatten().astype(np.float32)
    else:
        masked_patch = patch * mask
        patch_pixels = masked_patch[mask > 0].astype(np.float32)
        template_pixels = rotated_template[mask > 0].astype(np.float32)

    dot_product = np.dot(patch_pixels, template_pixels)
    norm1 = np.linalg.norm(patch_pixels)
    norm2 = np.linalg.norm(template_pixels)

    if norm1 == 0 or norm2 == 0:
        return 0.0

    return dot_product / (norm1 * norm2)


def refine_angle(search_img, template, pred_x, pred_y, pred_scale_x, pred_scale_y, pred_angle,
                         initial_range=15.0, step_size=1.5, imageShape=(224, 224), threshold=0.9):
    """自适应范围的角度细化"""
    
    def search_angles(angle_range, step):
        """在指定范围内搜索最佳角度"""
        angle_candidates = np.arange(
            pred_angle - angle_range, 
            pred_angle + angle_range + step, 
            step
        )
        
        best_score = -1
        best_angle = pred_angle
        
        for angle in angle_candidates:
            # 确保角度在[-180, 180]范围内
            normalized_angle = ((angle + 180) % 360) - 180
            
            mask, transformed_template = rotate_template(
                template, normalized_angle, 
                pred_scale_x, pred_scale_y
            )
            
            score = compute_masked_similarity(search_img, transformed_template, mask, pred_x, pred_y)
            # score = compute_masked_similarity(search_img, transformed_template, mask)
            
            if score > best_score:
                best_score = score
                best_angle = normalized_angle
        
        return best_angle, best_score
    
    # 第一阶段：在初始范围内搜索
    best_angle, best_score = search_angles(initial_range, step_size)
    
    # 如果初始范围内找到满足阈值的结果，直接返回
    if best_score >= threshold:
        return best_angle, best_score
    
    # 第二阶段：扩大到全范围搜索
    # print(f"Initial search failed (score={best_score:.3f}), expanding to full range...")
    coarse_angle, coarse_score = search_angles(180.0, 10)
    if coarse_score > best_score:
        coarse_angle, coarse_score = search_angles(10, 1)
    
    # 如果粗搜索找到更好的结果
    if coarse_score > threshold:
        return coarse_angle, coarse_score
    
    # 如果全范围搜索也没有改善，返回原始预测
    return pred_angle, best_score


def refine_angle_bisection(search_img, template, pred_x, pred_y, pred_scale_x, pred_scale_y, pred_angle,
                           initial_range=20.0, coarse_threshold=2.0, fine_step=0.5, imageShape=(224, 224), threshold=0.9):
    """使用二分法的角度细化（高效版）"""

    def get_score(angle):
        """计算给定角度下的匹配得分"""
        normalized_angle = ((angle + 180) % 360) - 180
        mask, transformed_template = rotate_template(
            template,normalized_angle,
            pred_scale_x, pred_scale_y
        )
        return compute_masked_similarity(search_img, transformed_template, mask, pred_x, pred_y)

    # 初始左右边界
    left = pred_angle - initial_range
    right = pred_angle + initial_range
    
    score_left = get_score(left)
    score_right = get_score(right)

    # 粗搜索阶段：二分
    while (right - left) > coarse_threshold:
        if score_left > score_right:
            right = (left + right) / 2
            score_right = get_score(right)
        else:
            left = (left + right) / 2
            score_left = get_score(left)

    # 精搜索阶段：细粒度遍历
    fine_angles = np.arange(left, right + fine_step, fine_step)
    best_score = -1
    best_angle = pred_angle

    for angle in fine_angles:
        score = get_score(angle)
        if score > best_score:
            best_score = score
            best_angle = angle
            
    if best_score > threshold:
        # 如果没有找到满足阈值的结果，返回原始预测
        return best_angle, best_score

    return refine_angle(search_img, template, pred_x, pred_y, pred_scale_x, pred_scale_y, pred_angle, 
                 initial_range=initial_range*2, step_size=1, imageShape=imageShape, threshold=threshold)


def refine_scale_x(search_img, template, pred_x, pred_y, pred_scale_x, pred_scale_y, refined_angle,
                   search_range=0.21, step_size=0.03, threshold=0.92):
    """细化X方向的缩放 """
    
    # 生成候选缩放值
    scale_candidates = np.arange(
        pred_scale_x - search_range,
        pred_scale_x + search_range + step_size,
        step_size
    )
    
    # 限制缩放范围在合理区间内
    scale_candidates = scale_candidates[scale_candidates > 0.3]
    scale_candidates = scale_candidates[scale_candidates < 3.0]
    
    best_score = -1
    best_scale_x = pred_scale_x
    
    for scale_x in scale_candidates:
        mask, transformed_template = rotate_template(
            template, refined_angle, 
            scale_x, pred_scale_y
        )
        
        score = compute_masked_similarity(search_img, transformed_template, mask, pred_x, pred_y)
        
        if score > best_score:
            best_score = score
            best_scale_x = scale_x
    
    # 如果改善不明显，返回原始值
    if best_score < threshold:
        return pred_scale_x, best_score
    
    return best_scale_x, best_score


def refine_scale_y(search_img, template, pred_x, pred_y, refined_scale_x, pred_scale_y, refined_angle,
                   search_range=0.15, step_size=0.015,  threshold=0.92):
    """细化Y方向的缩"""
    
    # 生成候选缩放值
    scale_candidates = np.arange(
        pred_scale_y - search_range,
        pred_scale_y + search_range + step_size,
        step_size
    )
    
    # 限制缩放范围在合理区间内
    scale_candidates = scale_candidates[scale_candidates > 0.3]
    scale_candidates = scale_candidates[scale_candidates < 3.0]
    
    best_score = -1
    best_scale_y = pred_scale_y
    
    for scale_y in scale_candidates:
        mask, transformed_template = rotate_template(
            template, refined_angle, 
            refined_scale_x, scale_y
        )
        
        score = compute_masked_similarity(search_img, transformed_template, mask, pred_x, pred_y)
        
        if score > best_score:
            best_score = score
            best_scale_y = scale_y
    
    # 如果改善不明显，返回原始值
    if best_score < threshold:
        return pred_scale_y, best_score
    
    return best_scale_y, best_score


def refine_position(search_img, template, pred_x, pred_y, refined_scale_x, refined_scale_y, refined_angle,
                   search_range=0.5, step_size=0.1, threshold=0.95):
    """细化位置: x, y组合优化"""
    
    # 生成x和y方向的偏移量
    # 从-0.9到0.9，步长0.3: [-0.9, -0.6, -0.3, 0, 0.3, 0.6, 0.9]
    offsets = np.arange(-search_range, search_range + step_size, step_size)
    
    best_score = -1
    best_x = pred_x
    best_y = pred_y
    
    # 遍历所有位置组合
    for dx in offsets:
        for dy in offsets:
            # 计算新位置
            new_x = pred_x + dx
            new_y = pred_y + dy
            
            mask, transformed_template = rotate_template(
                template, refined_angle, 
                refined_scale_x, refined_scale_y
            )
            
            score = compute_masked_similarity(search_img, transformed_template, mask, new_x, new_y)
            
            if score > best_score:
                best_score = score
                best_x = new_x
                best_y = new_y
    
    # 如果改善不明显，返回原始值
    if best_score < threshold:
        return pred_x, pred_y, best_score
    
    return best_x, best_y, best_score

````


### utils/tool.py

````python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
from matplotlib.transforms import Affine2D
from shapely.geometry import Polygon

######################################
#             for test
######################################

def rotated_rect(x_center, y_center, width, height, angle_degrees):
    """
    生成旋转矩形的四个顶点坐标
    :param x_center: 中心点x坐标
    :param y_center: 中心点y坐标
    :param width: 矩形宽度
    :param height: 矩形高度
    :param angle_degrees: 旋转角度（度数）
    :return: 旋转后的四个顶点坐标列表
    """
    angle_radians = np.radians(angle_degrees)
    cos_theta = np.cos(angle_radians)
    sin_theta = np.sin(angle_radians)

    # 定义未旋转时的四个顶点相对坐标
    corners = np.array([
        [width / 2, height / 2],   # 右上
        [-width / 2, height / 2],  # 左上
        [-width / 2, -height / 2], # 左下
        [width / 2, -height / 2]   # 右下
    ])

    # 旋转并平移顶点
    rotated_corners = []
    for x, y in corners:
        x_rot = x * cos_theta - y * sin_theta
        y_rot = x * sin_theta + y * cos_theta
        rotated_x = x_center + x_rot
        rotated_y = y_center + y_rot
        rotated_corners.append((rotated_x, rotated_y))
    
    return rotated_corners


def getIOU(true_param, pred_param, th=36, tw=36):
    """
    计算旋转矩形的交并比（IOU）
    :param true_param: 真实框参数 [x, y, scale, rotate]
    :param pred_param: 预测框参数 [x, y, scale, rotate]
    :param th: 模板高度（用于计算实际尺寸）
    :param tw: 模板宽度（用于计算实际尺寸）
    :return: IOU值
    """
    if len(pred_param) == 4:
        # 只有一个缩放参数
        pred_param = [pred_param[0], pred_param[1], pred_param[2], pred_param[2], pred_param[3]]
        true_param = [true_param[0], true_param[1], true_param[2], true_param[2], true_param[3]] 
    elif len(pred_param) == 3:
         # 没有缩放参数
        pred_param = [pred_param[0], pred_param[1],  1,  1, pred_param[2]]
        true_param = [true_param[0], true_param[1],  1,  1, true_param[2]] 
    
    true_param = np.array(true_param)
    pred_param = np.array(pred_param)
    
    # print(f"true_param: {true_param}")
    # print(f"pred_param: {pred_param}")
    # print(th, tw)
    
    # 解析参数
    true_x, true_y, true_sX, true_sY, true_r = true_param
    pred_x, pred_y, pred_sX, pred_sY, pred_r = pred_param

    # 计算实际宽高（假设scale为整体缩放因子）
    true_width = true_sX * tw
    true_height = true_sY * th
    pred_width = pred_sX * tw
    pred_height = pred_sY * th

    # 生成旋转矩形顶点
    true_poly = rotated_rect(true_x, true_y, true_width, true_height, -true_r)
    pred_poly = rotated_rect(pred_x, pred_y, pred_width, pred_height, -pred_r)

    # 创建多边形对象
    poly1 = Polygon(true_poly)
    poly2 = Polygon(pred_poly)

    # 检查多边形有效性
    if not poly1.is_valid or not poly2.is_valid:
        return 0.0

    # 计算交集和并集面积
    intersection = poly1.intersection(poly2).area
    union = poly1.area + poly2.area - intersection

    return intersection / union if union != 0 else 0.0


def get_center(center, points, threshold=15):
    """
    基于固定阈值去除离群点的均值计算
    
    参数：
    center : 中心点坐标，形状为(2,)的数组
    points : 原始点集，形状为(n, 2)的数组
    threshold : 离群点判定阈值（欧氏距离），默认为15
    
    返回：
    mean : 去除离群点后的均值，形状为(2,)的数组
    """
    if len(points) == 0:
        return center
    
    # 计算所有点到中心点的欧氏距离
    dx = points[:, 0] - center[0]
    dy = points[:, 1] - center[1]
    distances = np.sqrt(dx**2 + dy**2)
    
    # 过滤离群点
    mask = distances <= threshold
    filtered_points = points[mask]
    
    # 处理全为离群点的极端情况
    if len(filtered_points) == 0:
        return center  # 返回原始中心
    
    # 计算有效点的均值
    return np.mean(filtered_points, axis=0)


def draw_rotated_bbox(ax, param, color, th = 36, tw = 36, lineWidth=1):
    """
    在指定Axes上画旋转矩形和中心线。
    """
    if len(param) == 4:
        # 只有一个缩放参数
        param = [param[0], param[1], param[2], param[2], param[3]]
    elif len(param) == 3:
        # 没有缩放参数
        param = [param[0], param[1], 1, 1, param[2]]
    
    param = [float(p) for p in param]
    
    x, y, scale_x, scale_y, rotate = param
    h, w = th * scale_y, tw * scale_x

    # 创建矩形框
    rect = patches.Rectangle(
        (x - w/2, y - h/2),  # 左下角坐标
        w, h,                # 宽高
        linewidth=lineWidth,
        edgecolor=color,
        facecolor='none'
    )

    # 中心线
    line = plt.Line2D(
        [x, x + w/2],
        [y, y],
        color=color,
        linewidth=lineWidth,
        linestyle='-'
    )

    # 旋转变换
    transform = Affine2D().rotate_deg_around(x, y, -rotate) + ax.transData
    rect.set_transform(transform)
    line.set_transform(transform)

    ax.add_patch(rect)
    ax.add_line(line)

````


### utils/tools.py

````python
#coding=utf-8
import cv2, torch, math, random
import numpy as np
import torch.nn as nn
from torchvision.utils import save_image
  
######################################
#             for train
######################################
   

def weight_init(module):
    for n, m in module.named_children():
        # print('initialize: '+n)
        if isinstance(m, (nn.Conv2d, nn.ConvTranspose2d)):
            nn.init.kaiming_normal_(m.weight, mode='fan_in', nonlinearity='relu')
            if m.bias is not None:
                nn.init.zeros_(m.bias)
        elif isinstance(m, (nn.BatchNorm2d, nn.InstanceNorm2d)):
            if m.weight is not None:
                nn.init.ones_(m.weight)
            if m.bias is not None:
                nn.init.zeros_(m.bias)
        elif isinstance(m, nn.Linear):
            nn.init.kaiming_normal_(m.weight, mode='fan_in', nonlinearity='relu')
            if m.bias is not None:
                nn.init.zeros_(m.bias)
        elif isinstance(m, nn.Sequential):
            weight_init(m)
        elif isinstance(m, nn.ReLU) or isinstance(m, nn.Sigmoid) or isinstance(m, nn.Tanh) or isinstance(m, nn.PixelShuffle):
            pass
        else:
            m.initialize()


def gaussian2D(shape, center, sigma, scale_x, scale_y, rotation=0):
    """
    生成二维高斯热图

    参数:
        shape (tuple): 热图画布的尺寸 (高度, 宽度)
        center (tuple): 高斯分布的中心坐标 (x, y)
        sigma (float or torch.Tensor): 高斯分布的基础标准差（决定热力图的大小）
        scale_x (float or torch.Tensor): x方向的缩放系数
        scale_y (float or torch.Tensor): y方向的缩放系数
        rotation (float or torch.Tensor): 旋转角度（度），正值表示逆时针旋转

    返回:
        torch.Tensor: 二维高斯热图
    """
    height, width = shape
    device = center.device  # 获取输入张量的设备
    
    # 将旋转角度转换为张量（如果输入是float）
    if not isinstance(rotation, torch.Tensor):
        rotation = torch.tensor(rotation, device=device)
    
    # 生成网格坐标
    x = torch.arange(width, dtype=torch.float32, device=device)
    y = torch.arange(height, dtype=torch.float32, device=device)
    xx, yy = torch.meshgrid(x, y, indexing='xy')  # 生成网格坐标 (H, W)

    # 平移到中心点
    xx_centered = xx - center[1]
    yy_centered = yy - center[0]

    # 转换为弧度并计算旋转矩阵元素
    theta = torch.deg2rad(-rotation)
    cos_theta = torch.cos(theta)
    sin_theta = torch.sin(theta)

    # 应用旋转矩阵（等效于坐标旋转-θ角度）
    xx_rot = xx_centered * cos_theta + yy_centered * sin_theta
    yy_rot = -xx_centered * sin_theta + yy_centered * cos_theta

    # 计算各向异性的标准差（主轴: sigma*scale，次轴: sigma）
    sigma_x = sigma * scale_x
    sigma_y = sigma * scale_y

    # 计算高斯分布
    exponent = (xx_rot ** 2) / (2 * sigma_x ** 2) + (yy_rot ** 2) / (2 * sigma_y ** 2)
    gaussian = torch.exp(-exponent)

    gaussian[gaussian < 0.5] = 0
    return gaussian


def create_gt(images, true_params, template_shape):
    # true_params: [center_y, center_x, scale_y, scale_x, angle]
    b, c, h, w = images.shape
    th, tw = template_shape
    gt_score, gt_param = [], []
    for i in range(b):
        angle = true_params[i, 4]
        sign = 1 if angle > 0 else 0
        cos  = np.cos(np.deg2rad(angle))
        scale_y, scale_x = true_params[i, 2:4]
        sigma = 3.2  # 16 / 4
        HSx, HSy = (tw * scale_x) / min(th, tw), (th * scale_y) / min(th, tw)   # 热力图在两个方向上的缩放系数
        heatmap = gaussian2D((h, w), true_params[i, 0:2], sigma, HSx, HSy, angle)
        gt_score.append(heatmap)
        H, W = heatmap.shape
        gt = torch.zeros((4, H, W))
         
        y,x = torch.where(heatmap > 0)
        gt[0, y, x] = sign
        gt[1, y, x] = cos
        gt[2, y, x] = scale_x
        gt[3, y, x] = scale_y

        gt_param.append(gt)

    # [sign, cos, scale_x, scale_y]
    gt_score = torch.stack(gt_score)
    gt_param = torch.stack(gt_param)
    return gt_score, gt_param


if __name__ == "__main__":
    heatmap = gaussian2D(
        shape=(196, 196),
        center=torch.tensor([164.5, 82.8]),  # 亚像素中心
        sigma=4.0,
        scale_x=2,
        scale_y=1,
        rotation=60.0
    )
    save_image(heatmap, 'heatmap.png')
    
    gt_y, gt_x = torch.nonzero(heatmap == heatmap.max())[0]
    print("gt_y: ", gt_y)  # 33
    print("gt_x: ", gt_x)  # 64
    
````
