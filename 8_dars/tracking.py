# from ultralytics import YOLO
# import cv2
# model = YOLO('yolov8n.pt')
# results = model(source='img1.jpg',show = True, save= True,conf = 0.3),project = 'tracking', name= 'people'

# for cls in detected_classes:
#     clas_name = model.names[int(cls)]
#     clas_count[clas_name]= clas_counts.get(clas_name,0)+1


# for clas_name,count in clas_counts.item():
#     print(f'{clas_name}: {count}')
from ultralytics import YOLO
import cv2

# Modelni yuklash
model = YOLO('yolov8n.pt')

# Rasmni YOLO bilan analiz qilish
results = model('img1.jpg', show=True, save=True, conf=0.3)

# Detected klasslarni olish
detected_classes = []
clas_counts = {}

for result in results:
    for box in result.boxes:
        cls = int(box.cls[0])  # Klass indeksini olish
        class_name = model.names[cls]  # Klass nomini olish
        detected_classes.append(class_name)
        clas_counts[class_name] = clas_counts.get(class_name, 0) + 1

# Natijalarni chop etish
for class_name, count in clas_counts.items():
    print(f'{class_name}: {count}')
