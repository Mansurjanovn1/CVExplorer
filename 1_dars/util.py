 #Kutubxonalar
import numpy as np
import cv2

def get_limits(color):
    c = np.uint8([[color]])   #Rangli Numpy massivi sifatida yaratish
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)  # BGR dan HSV ga otkazish
     
    # HSV diapazon chegaralarini aniqlash
    lower_Limit = (max(hsvC[0][0][0] - 10,0), 100, 100)
    upper_Limit = (min(hsvC[0][0][0] + 10, 179), 255,255)

    # Massivlarni np.array ko‘rinishiga o‘tkazish   
    lower_Limit = np.array(lower_Limit, dtype = np.uint8)
    upper_Limit = np.array(upper_Limit, dtype = np.uint8)

    return lower_Limit, upper_Limit
