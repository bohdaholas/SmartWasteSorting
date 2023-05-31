from ultralytics import YOLO

model = YOLO('best.pt') # load model

model.predict(source="test/", save=True)