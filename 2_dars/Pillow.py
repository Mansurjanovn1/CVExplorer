#Kerakli kutubxonalni yuklash
from PIL import Image,ImageEnhance, ImageFilter,ImageDraw,ImageOps
import cv2

# image_path = "/Users/mansurjonovnurmuhammad/Desktop/2_dars/man.jpg" #Rasmni kiritish
# img = cv2.imread(image_path) #Rasmni oqitish
# cv2.imshow("img", img)  #Korsatish
# cv2.waitKey(0)  #Kutush vaqtini berish
 
img = Image.open("man.jpg") #Rasmni yuklash
#Flip
# img_flip = ImageOps.flip(img) #Rasmni flip(aylantirish) qilish
# img_flip.show()  #Korsatish

#Draw
# draw = ImageDraw.Draw(img)
# draw.rectangle([200,200,300,300], outline = "black", width = 5,) #Rasmga bbox yaratish
# img.show() #Korsatish

#Image Blur
# img_blur = img.filter(ImageFilter.GaussianBlur(5)) #GaussianBlur yordamida rasmni blur qilish
# img_blur.show() #Korsatish

#Brigtnes
# enhanser = ImageEnhance.Brightness(img)
# img_bright = enhanser.enhance(1) #Rasmga qancha yoruglik berilishi
# img_bright.show() #Korsatish

#Resize
# img_resized = img.resize((300,400)) #Yangi olchamni kiritish
# img_resized.show() #Korsatish

