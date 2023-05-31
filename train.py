import sys
from ultralytics import YOLO

model_path = sys.argv[1]
epochs_num = sys.argv[2]
batches_num = sys.argv[3]

model = YOLO(model_path)

model.train(data="data.yaml", epochs=int(epochs_num), imgsz=640, batch=int(batches_num))
model.val(split="test")
