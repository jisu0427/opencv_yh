# 흰색 오브젝트에 있는 작은 검은색 구멍을 메우는데 사용 : closing
# dilation -> erosion

import cv2

image = cv2.imread('data/images/closing.png')
cv2.imshow('Original', image)
closeSize = 3
element = cv2.getStructuringElement(shape = cv2.MORPH_ELLIPSE, ksize = (2*closeSize, 2*closeSize))
imageClose = cv2.morphologyEx(image, cv2.MORPH_CLOSE, element, iterations=3)
cv2.imshow('close', imageClose)
cv2.waitKey(0)
cv2.destroyAllWindows()