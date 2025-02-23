 #Kutubxonalar
import cv2
from PIL import Image
from util import get_limits

green = [0, 255, 0]     #Yashil rang chiqarish
cap = cv2.VideoCapture(0)  #WebCamera sonini kiritish

if not cap.isOpened:
    print("Error: Could not open webcam") # Agar kamera ochilmasa ("Error: Could not open webcam") dab chiqarsin va chiqib ketsin
    exit()   

while True:
    success, frame = cap.read()
    if not success:              
        print("Error: Failed to capture image")    # Agar rasm ochilmasa ("Error: Failed to capture image") dab chiqarsin va chiqib ketsin
        break

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)   #BGR tasvirni HSV formatga o‘tkazish
    lowerLimit, upperLimit = get_limits(color=green)   #Yashil rang uchun HSV diapazonlarini olish

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit) #Yashil rang uchun maska yaratish
    mask_= Image.fromarray(mask)  #Maskani tasvir shaklida olish
    bbox = mask_.getbbox()
    #print(bbox)
    if bbox is not None:
        x1,y1,x2,y2 = bbox
        frame = cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,0),3)

      
      #Natijani ko'rsatish
    cv2.imshow("Webcam Feed", frame)

       #Qayta ishlash va chiqish
    if cv2.waitKey(1) & 0XFF == ord("q"):
        break

cap.release()   #Bu metod kamerani bo'shatadi, shunda boshqa dasturlar uni ishlata oladi.
cv2.destroyAllWindows()  #Hamma ochiq oynalarni yopish