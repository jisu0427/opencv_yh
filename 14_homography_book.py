import cv2
import numpy as np
image = cv2.imread('data/images/book2.jpg')
cv2.imshow('original', image)

# 원본 이미지의 4개위 점 좌표!
point_original = np.array([141, 131, 480, 159, 493, 630, 64, 601], dtype = float)
point_original = point_original.reshape(4, 2)

print(point_original)

# 다른 이미지 불러와서,
# 위의 원본이미지 4개 점의 좌표와 매칭되는 점의 좌표도 셋팅
image_dst = cv2.imread('data/images/book1.jpg')
cv2.imshow('destination', image_dst)

point_dst = np.array([318, 256, 534, 372, 316, 670, 73, 473], dtype=float)

point_dst = point_dst.reshape(4,2)
print(point_dst)

# 두 이미지의 서로 매칭되는
# 이 점들의 정보를 가지고
matrix, status = cv2.findHomography(point_original, point_dst)

# 행렬을 구했으면, 이미지를 처리할 수 있다. 
result = cv2.warpPerspective(src = image, M = matrix, dsize = (image.shape[1], image.shape[0]))
cv2.imshow('Warp', result)
cv2.waitKey(0)
cv2.destroyAllWindows()