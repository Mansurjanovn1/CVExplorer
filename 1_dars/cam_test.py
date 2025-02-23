 #Kutubxona
import cv2

cap = cv2.VideoCapture(0) #WebCamera sonini kiritish

if not cap.isOpened():
    print("Error: Could not open webcam") #Bu metod kamera muvaffaqiyatli ochilganligini tekshiradi. 
    exit()  #Agar kamera ochilmasa (False bo'lsa), "Error" deb chiqaradi va dasturdan chiqadi (exit()).

while True:   #Bu cheksiz sikl bo'lib, kamera orqali video oqimini davom ettiradi

    succsess, frame = cap.read()

    if not succsess:
        print("Error") #Agar kadrni o'qish muvaffaqiyatli bo'lmasa (not succsess),
        break          #"Error" deb chiqariladi va sikldan chiqiladi (break).


    cv2.imshow("Webcam Feed", frame) #Bu metod o'qilgan kadrni ko'rsatadi.

         #Qayta ishlash va chiqish
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cap .release()  #Bu metod kamerani bo'shatadi, shunda boshqa dasturlar uni ishlata oladi.
cv2.destroyAllWindows() #Qolgan oynalarni yopadi
