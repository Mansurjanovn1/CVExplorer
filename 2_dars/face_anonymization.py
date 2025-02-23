#Kutubxonalar
import cv2   #OpenCV kutubxonasi rasm va video bilan ishlash uchun
import mediapipe as mp  #MediaPipe yuz aniqlash (face detection) uchun
import os   # OS fayl va papkalar bilan ishlash uchun
import argparse  # Argumentlarni komandadan o‘qish uchun

def process_image(img_rgb,face_detection): # Tasvirni qayta ishlash uchun funksiya
     img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # BGR formatidan RGB ga aylantiramiz
     out = face_detection.process(img_rgb)  # MediaPipe orqali yuzni aniqlash
    # print(out.detections)
     if out.detections is not None:   # Agar yuz aniqlangan bo‘lsa
        for detection in out.detections:   # Har bir aniqlangan yuz uchun:
                location_data = detection.location_data  # Yuzning koordinatalarini olish
                bbox = location_data.relative_bounding_box  # Yuzning bounding boxni olish

                # Yuzi chizilgan to‘rtburchak koordinatalarini olish
                x1, y1, w, h = bbox.xmin, bbox.ymin, bbox.width, bbox.height
                x1 = int(x1 * W)   # Asosiy rasm o‘lchamiga ko‘ra hisoblash
                y1 = int(y1 * H)
                w = int(w * W)
                h = int(h * H)
               #Blur
              # img=cv2.blur(img,(2,2))
                img[y1:y1+h,x1:x1+w,:]=cv2.blur(img[y1:y1+h,x1:x1+w,:],(20,20))  # Yuzni blur qilish
                return img   # Qayta ishlangan tasvirni qaytarish
args=argparse.ArgumentParser()   ## Argumentlarni o‘qish uchun parser yaratish
args.add_argument("--mode",default='image')  # Tasvir yoki video rejimini tanlash
args.add_argument("--filePath",default='photo.jpg') # Rasmni kiritish
args=args.parse_args()  # Argumentlarni o‘qish
output_dir='./output'  # Natijalar saqlanadigan papka
if not os.path.exists(output_dir):   # Agar papka mavjud bolmasa
     os.makedirs(output_dir)   # Yangi papka yaratish

# img_path='stive.jpeg'
# img=cv2.imread(img_path)
# H,W,_=img.shape
mp_face_detection=mp.solutions.face_detection  # MediaPipe yuz aniqlash funksiyasi

with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
     if args.mode in ["image"]:    # Agar image holatida bolsa:
          img=cv2.imread(args.filePath)  # Tasvirni yuklash
          H,W,_=img.shape   # Tasvir o‘lchamlarini olish
          img=process_image(img,face_detection)    # Yuzni aniqlash va blur qilish
          output_path = os.path.join(output_dir, 'Photo.png')  # Natijani saqlash
          cv2.imwrite(output_path, img)    # Natijani fayl sifatida saqlash
        
     elif args.mode in ['video']:   # Agar fayl video holatida bolsa:
          cap=cv2.VideoCapture(args.filePath)  # Videoni ochish
          success,frame=cap.read()    # Videodan birinchi freymni o‘qish
          while True:    # Videoni doimiy qayta ishlash
               frame=process_image(frame,face_detection)    # Yuzni aniqlash va blur qilish
               success,frame=cap.read()   # Keyingi freymni o‘qish

                # img=cv2.rectangle(img,(x1,y1),(x1+w,y1+h),(255,0,0),10)
# cv2.imshow('img',img)
# cv2.waitKey(0)