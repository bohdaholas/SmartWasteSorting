from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # load a pretrained model

model.train(data="data.yaml", epochs=10, imgsz=640, batch=16)
model.val(split="test")