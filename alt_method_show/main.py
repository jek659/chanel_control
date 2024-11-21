#install packet
#pip install opencv-python
#pip install matplotlib 
import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"alt_method_show\8.jpeg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
g_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
hsv_img = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
r,g,b = cv2.split(img)
h,s,v = cv2.split(hsv_img)
titles = ["ch r","ch g","ch b","original","gray","hsv","ch h","ch s","ch v"]
images = [r,g,b,img,g_img,hsv_img,h,s,v]
count  = 9
for i in range(count):
    plt.subplot(3,3,i+1)
    plt.title(titles[i])
    plt.imshow(images[i],"gray")
plt.show()

