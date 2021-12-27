import cv2
import numpy as np


# cv2.IMREAD_COLOR 랑 1은 같은 의미
source = cv2.imread('data/images/sample.jpg',1)
print(cv2.IMREAD_COLOR)

# 가로 80% 세로 60%
# 이미지 확대, 축소
scaleX= 0.8   # 가로
scaleY= 0.6   # 세로

scaleDown = cv2.resize(source, None, fx = scaleX, fy= scaleY, interpolation=cv2.INTER_LINEAR)
print(scaleDown)
cv2.imshow('Scaled Down', scaleDown)
cv2.imshow('Original', source)


# CROP 이미지 자르기!
crop_img = source[ 10:200, 150:250 ]
cv2.imshow('crop img', crop_img)




cv2.waitKey(0)
cv2.destroyAllWindows()