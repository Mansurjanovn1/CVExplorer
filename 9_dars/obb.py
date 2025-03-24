from ultralytics import YOLO
model = YOLO('yolov8s-obb.pt')
results = model('vid.mp4',save = True, show = True,conf = 0.3)