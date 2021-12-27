import cv2
import numpy as np

img = cv2.imread('data/images/mark.jpg')
cv2.imshow('img', img)

# 선 그리기
imageLine = img.copy()
cv2.line(imageLine, (322,179), (400,183), (0,0,255), 3, cv2.LINE_AA) # -> 선 그리는 코드
cv2.imshow('image Line', imageLine)


# 원 그리기
imageCircle = img.copy()
cv2.circle(imageCircle, (350, 200), 150, (255, 0, 0), 3, cv2.LINE_AA)
cv2.imshow('image Circle', imageCircle)

# 타원 그리기
imageEllipse = img.copy()
cv2.ellipse(imageEllipse, (360, 200), (100,170), 45, 0, 360, (0, 255, 0), 2)
cv2.ellipse(imageEllipse, (360, 200), (100,170), 135, 0, 360, (0, 0, 255), thickness=2)
cv2.imshow('image Ellipse', imageEllipse)

# 사각형 그리기
imageRectangle = img.copy()
cv2.rectangle(imageRectangle, (208,55), (450,355), (255,0,0), 3)
cv2.imshow('image Rectangle', imageRectangle)

# 글자 넣기
imageText = img.copy()
cv2.putText(imageText, 'Mark Zuckerberg', (205,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
cv2.imshow('image Text', imageText)



cv2.waitKey(0)
cv2.destroyAllWindows()