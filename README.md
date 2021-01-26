# tiny-yolov3
使用 tiny——yolov3（keras）检测自己的数据集

程序是根据 GitHub 上 YOLOv3 修改的，所以大面积重复，使用 tiny-yolo 用法如下：

# 标注数据集
使用 [labelImg](https://github.com/tzutalin/labelImg) 对数据集进行标注，标注完成后会生成对应的 XML 文件。

# 使用

## 环境
系统：Ubuntu 20.04 LTS  
Python：3.6.11  
Keras：2.1.5  
TensorFlow：1.5.1  

## 准备
1. 将你的图片数据集都放在 `VOC2007/JPEGImages` 文件夹
2. 将标注后生成的 XML 文件放在 `VOC2007/Annotations` 文件夹
3. 修改 `voc_annotation.py` 里的 `classes` 为你的检测类别
4. 修改 `model_data` 文件夹下的 `voc_classes.txt` 和 `coco_classes.txt` 为你的检测类别（一行一个）
5. 生成 `VOC2007/ImageSets/Main` 下的文件
```shell
cd VOC2007
python test.py
```
6. 生成 tiny-yolo3 所需的 `train.txt`，`val.txt`，`test.txt`
```shell
python voc_annotation.py
# 然后将 test.txt 里的数据复制到 train.txt 中
```

## 训练
1. 安装依赖
```shell
pip install -r requirements.txt
```
2. 开始训练，3000 轮
```shell
python tiny_train.py
```
3. 权重文件
训练完成后，权重文件会保存在 `logs` 文件夹下

## 测试
1. 将测试集放在 `VOC2007/Images` 文件夹下
2. 执行测试
```shell
python yolo_test_batch.py
```
3. 检测后的标注结果会生成在 `VOC2007/SegmentationClass`


## WebAPI
执行 `test_web_api.py` 会在本地开启一个 Web 服务，可以通过该服务来使用 API 接口  

|  参数   | 类型  | 必须 | 请求类型 |
|  ----  | ----  | :----: | ---- |
| file  | 文件 | √ | POST |


返回结果：
```json
{
    "code": 0,
    "data": {
        "gap": {
            "bottom": 275,
            "left": 499,
            "right": 582,
            "score": 0.9966819882392883,
            "top": 180
        }
    }
}
```

## 感谢
https://github.com/Eatzhy/tiny-yolov3

本项目 fork 自该项目，但因为上传了 h5 模型，导致 .git 文件过大，所以新开了一个 repo，稍微改动了一下。