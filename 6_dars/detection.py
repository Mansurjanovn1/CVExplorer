from ultralytics import YOLO
model = YOLO('yolov8n-seg.pt')
model.predict(source=0, show = True, save=True, conf = 0.3)