import numpy as np
import cv2



height = 300
width = 1100

image = np.zeros([height, width, 3], dtype=np.uint8)

print(image.shape)

for y in range(image.shape[0]):
    for x in range(image.shape[1]):
        image[y, x] = [255, 255, 255]


for x in range(0, image.shape[1], 100):
    cv2.line(image, (x, 0), (x, image.shape[0]), (0, 0, 0), thickness=2)



for y in range(0, image.shape[0], 100):
    cv2.line(image, (0, y), (image.shape[1], y), (0, 0, 0), thickness=2)

def circle_shape(event,x,y,flagval,par):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(image, (x,y), 40, (255,0,0), thickness=4)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(image, (x,y), 40, (0,255,255), thickness=4)
    elif event == cv2.EVENT_RBUTTONDBLCLK:
        cv2.circle(image, (x, y), 40, (33,177,75), thickness=4)
    elif event == cv2.EVENT_MOUSEWHEEL:
        #cv2.circle(image, (x,y), 40, color=(0,0,255), thickness=4)
        cv2.ellipse(image, (x,y), (95,40) ,
                    0, 0, 360, (0, 0, 255) , 4)
cv2.namedWindow(winname='Image_Window')
cv2.setMouseCallback('Image_Window', circle_shape)
while True:
    cv2.imshow('Image_Window', image)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.imshow("image", image)
cv2.destroyAllWindows()

