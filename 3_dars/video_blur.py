# Kutubxonallar
import cv2
import mediapipe as mp 
import os

# Kirish va chiqish fayllari
input_video = "video.mp4"
output_dir = "output"

os.makedirs(output_dir, exist_ok=True) #yangi papka yaratish
output_video = os.path.join(output_dir, "blured_face.mp4") #yangi video faylini yaratish

# Video mavjudligini tekshirish
if not os.path.exists(input_video):
    print("Error: Video not found")
    exit(1)

# Mediapipe yuzni aniqlash modeli
mp_face = mp.solutions.face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5)
cap = cv2.VideoCapture(input_video)
#Agar video ochilmasa "Error: Could not open video file" chiqadi
if not cap.isOpened():
    print("Error: Could not open video file")
    exit(1)

# Video parametrlari
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) * 0.75)
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) * 0.75)
fps = int(cap.get(cv2.CAP_PROP_FPS))

fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # Universally compatible codec
out = cv2.VideoWriter(output_video, fourcc, fps, (frame_width, frame_height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Kadr o'lchamini o'zgartirish
    frame = cv2.resize(frame, (frame_width, frame_height))

    # RGB formatga o'girish
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = mp_face.process(frame_rgb)

    # Yuzlarni aniqlash va blur qilish
    if results.detections:
        for detection in results.detections:
            bbox = detection.location_data.relative_bounding_box
            x, y, w, h = (
                int(bbox.xmin * frame_width), int(bbox.ymin * frame_height),
                int(bbox.width * frame_width), int(bbox.height * frame_height)
            )

            x, y = max(0, x - 10), max(0, y - 10)
            w, h = min(frame_width - x, w + 20), min(frame_height - y, h + 20)

            # ROI (Region of Interest) - yuz hududi
            face_roi = frame[y:y+h, x:x+w]

            # Yuzni blur qilish
            if face_roi.shape[0] > 0 and face_roi.shape[1] > 0:  # ROI tekshirish
                blured_face = cv2.GaussianBlur(face_roi, (55, 55), 30) # Gaussian blur orqali yuzni blur qilish
                frame[y:y+h, x:x+w] = blured_face 

    # Chiqarish fayliga yozish
    out.write(frame)

    # Ekranda ko'rsatish
    cv2.imshow("Blured face video", frame)
    # Agar "q" tugmasini bosilsa chiqish
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break  

# Barcha oynalarni yopish
cap.release()
out.release()
cv2.destroyAllWindows()

# Yuklanganligi haqida ma'lumot berish
print(f"Blurred face video saved at {output_video}")

