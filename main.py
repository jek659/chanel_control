#Открытие изображения в openCV
#pip install opencv-python  -  установка библиотеки
import cv2 

pic = cv2.imread(r"1.jpeg")
mode = 0
b,g,r = cv2.split(pic)
while True:
    if(mode == 0):
        cv2.imshow("1",pic)
    elif(mode == 1):
        cv2.imshow("1",r)
    elif(mode == 2):
        cv2.imshow("1",g)
    elif(mode == 3):
        cv2.imshow("1",b)
    key = cv2.waitKey(33)
    print(key)
    if(key == 27):
        break
    elif(key == 114):
        mode = 1
    elif(key == 103):
        mode = 2
    elif(key == 98):
        mode = 3
    elif(key == 32):
        mode = 0
cv2.destroyAllWindows()