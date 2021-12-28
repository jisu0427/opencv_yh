# 이미지 형태 전환 : 이미지 확장(dilation)
# https://webnautes.tistory.com/1257

import cv2
image = cv2.imread('data/images/truth.png')
cv2.imshow('original', image)

# 이미지 확장(팽창) : dilation
dilationSize = 6

# element = cv2.getStructuringElement(shape = cv2.MORPH_RECT, ksize=(2*dilationSize, 2*dilationSize))
# element = cv2.getStructuringElement(shape = cv2.MORPH_ELLIPSE, ksize=(2*dilationSize, 2*dilationSize))
element = cv2.getStructuringElement(shape = cv2.MORPH_CROSS, ksize=(2*dilationSize, 2*dilationSize))


imageDilate = cv2.dilate(image, element)

cv2.imshow('dilation', imageDilate)

cv2.waitKey(0)
cv2.destroyAllWindows()