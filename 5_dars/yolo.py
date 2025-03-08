from ultralytics import YOLO
model = YOLO('yolov8l.pt')
model.predict(source='img1.jpeg', show = True,save = True, conf = 0.4)