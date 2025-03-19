from ultralytics import YOLO
model = YOLO('yolov8n-cls.pt')
results = model(source='vid.mp4',conf= 0.3,save= True, show=True) 