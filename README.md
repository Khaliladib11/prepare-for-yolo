# prepare-for-yolo 🚀🚀🚀

<p align="center">
  <img src="https://github.com/Khaliladib11/prepare-for-yolo/blob/main/images/yolo.png" alt="Sublime's custom image"/>
</p>

The main goal of this repo is to prepare your data for training using [**YOLOv5**](https://pages.github.com/](https://github.com/ultralytics/yolov5)) 💡.

In order to train your custom dataset using yolov5, you must create the following hierarchy ✏️:

```
├─dataset
│ ├─images
│ │ ├─train
│ │ ├─val
│ │ ├─test
│ ├─labels
│ │ ├─train
│ │ ├─val
│ │ ├─test
```

---
## Requirements ⭐
Please install requirements using: 
```bash
pip install -R requirements.txt
```
---
## How to use 🔥

First of all, you have to edit the [**dataset class**](https://github.com/Khaliladib11/prepare-for-yolo/blob/main/src/dataset.py). Please make sure to keep the same variable names ⛔. The `__getitem__` in the [**dataset**](https://github.com/Khaliladib11/prepare-for-yolo/blob/main/src/dataset.py) must return two things 🚬:
* Path to image ⚡
* Bounding boxes, which is a list that has `k` list. Each one of the `k` is a list that has [`cls_id`, `x`, `y`, `w`, `h`] ⚡

After that, you have to create three instances from this class, for **train**, **val** and **test** 💣

Now you can just create instance from the prepare class and use it:
```python
from src.prepare import Prepare
from src.dataset import Dataset

traindataset = Dataset(**kwargs)
valdataset = Dataset(**kwargs)
testdataset = Dataset(**kwargs)
path = "path..."

prep = Prepare(train_dataset=traindataset, val_dataset=valdataset, test_dataset=testdataset, path=path)
prep.create()
```

This will create the above hierarchy. Then you can just copy the `dataset` folder to the yolov5 repo when you clone it. Don't forget to add the  `yaml` file to tell yolo model the path to **train**, **val** and **test**, also the number of classes and the name of the classes. Here is an example:

```yaml
train:  ../dataset/images/train/
val:  ../dataset/images/val/
test: ../dataset/images/test/

# number of classes
nc: 4

# class names
names: ['pedestrian', 'car', 'traffic light', 'traffic sign']
```
