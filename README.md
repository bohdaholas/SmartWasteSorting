# SmartWasteSorting
Authors:
* [Bohdan Ivashko](https://github.com/bohdaholas) </br>
* [Viktoriia Roi](https://github.com/ViktoriiaRoi) </br>

## Data
* In the `data_path` should be located folders for every class separately.
* Inside every folder should be an image (.img) and its label (.txt) with the same filename.
* To prepare data, the scipts `resize_images.py` and `split_images.py` are used. 
* This code resized images to model input size 640x640 and split data to folders train, val and test in the `output_path`.
```
python resize_images.py <data_path>
python split_images.py <data_path> <output_path>
```

Already prepared dataset is located [here](https://drive.google.com/file/d/18Rg_8B40hAGZrmYmh4Byg3UzP0VItCBf/view?usp=sharing).

## Usage
To use the model, in `data.yaml` file should be specified paths to train, val and test folders. For example:
```
train: ./output/train
val: ./output/val
test: ./output/test
```
Then to train and predict data, the scripts `train.py` and `predict.py` are used.
```
python train.py <model> <epochs> <batch>
python predict.py <model> <source>
```

## Example
```
python train.py yolov8n.pt 10 16
python predict.py runs/train/weights/best.pt source/
```
