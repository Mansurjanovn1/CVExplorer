from ultralytics import YOLO
model = YOLO('yolov8x.pt')
results = model.track(source='pic.jpg',save = True, show = True, conf = 0.3)