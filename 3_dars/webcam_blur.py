#kutubxonalar 
import cv2
import mediapipe as mp 

mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection(model_selection = 0,min_detection_confidence = 0.5)


cap = cv2.VideoCapture(0) #webcamera sonini kiritish

#Agar webcamera ochilmasa "Error: Couldn't open the cam" chiqadi
if not cap.isOpened(): 
    print("Error: Couldn't open the cam")
    exit(1)

#chiqish uchun "w" tugmasini bosish
print("Press 'w' to exit")

#agar ishlasayu lekin ochilmasa chiqib ketish"Break"
while True:
    sucsess, frame = cap.read()
    if not sucsess:
        break

    #BGR formtidan RGB formatiga o'tkazish
    frame_rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    # yuzni aniqlash
    results = face_detection.process(frame_rgb)

    # Agar yuzlar aniqlansa
    if results.detections:
        #Yuz va rictanglelarni bir biriga bog'lash
        for detection in results.detections:
            bboxC = detection.location_data.relative_bounding_box
            h,w, _  = frame.shape
            
            x, y, width, height = (int(bboxC.xmin * w),
                                   int(bboxC.ymin * h),
                                   int(bboxC.width * w),
                                   int(bboxC.height * h))  
            x,y = max(0,x), max(0,y)
            width,height = min(w - x, width), min(h - y, height)
            face_region = frame[y:y+height, x:x+width]
            blurred_face = cv2.GaussianBlur(face_region,(55,55), 10) #Gaussian blur orqali yuzni blur qilish
            frame[y:y+height, x:x+width] = blurred_face

    cv2.imshow("Face Blur Webcam(MediaPipe)",frame) # Qayta ishlangan videoni ko'rsatish

    if cv2.waitKey(1) & 0xFF == ord("w"):  # "w" tugmasini bosish orqali chiqish
        break


#Barcha oynalarni yopish
cap.release()
cv2.destroyAllWindows()
