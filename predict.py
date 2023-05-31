import sys
from ultralytics import YOLO

model_path = sys.argv[1]
source_path = sys.argv[2]

model = YOLO(model_path)
model.predict(source=source_path, save=True)
