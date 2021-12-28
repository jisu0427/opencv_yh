# 이미지 형태 전환 : 이미지 침식(erode)
# https://webnautes.tistory.com/1257

import cv2
image = cv2.imread('data/images/truth.png')
cv2.imshow('original', image)

# 이미지 침식 : erode
erodeSize = 6

element = cv2.getStructuringElement(shape = cv2.MORPH_RECT, ksize=(2*erodeSize, 2*erodeSize))


imageErode = cv2.erode(image, element)

cv2.imshow('erode', imageErode)

cv2.waitKey(0)
cv2.destroyAllWindows()