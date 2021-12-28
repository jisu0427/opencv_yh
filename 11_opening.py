# 노이즈(작은 흰색 물체) 있는 이미지 제거 : opening
# Erosion -> Dilation
# https://webnautes.tistory.com/1257

import cv2
image = cv2.imread('data/images/opening.png')
openingSize = 3
element = cv2.getStructuringElement(shape = cv2.MORPH_ELLIPSE, ksize = (2*openingSize, 2*openingSize))
imageOpened = cv2.morphologyEx(src = image, op = cv2.MORPH_OPEN, kernel = element, iterations=5)


cv2.imshow('original', image)
cv2.imshow('open', imageOpened)

cv2.waitKey(0)
cv2.destroyAllWindows()