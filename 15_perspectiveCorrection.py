import cv2
import numpy as np

from utils import get_four_points

image = cv2.imread('data/images/book1.jpg')

# cv2.imshow('Original', image)

# image 좌표 4곳 
# 시계방향으로 찍을 것
# 좌표만 알아내고 주석처리함
# 주석처리 안하고는 좌표찍으면 결과 이미지 나옴
point_src = get_four_points(image)
print(point_src)

# image의 4개의 점은 마우스 클릭으로 해결완료
# point_original = np.array([[318., 256.],[535., 374.],[318., 669.],[ 74., 475.]])
point_dst = np.array([[0, 0], [300, 0], [300, 400], [0, 400]])
# image_dst의 4개의 점은 우리가 구할것
# 행렬 구하기
matrix, status = cv2.findHomography(point_src, point_dst)
# 변환함수를 통해 이미지를 가져올 것
# 새로운 이미지의 사이즈는 x=400, y=300
result = cv2.warpPerspective(src = image, M = matrix, dsize = (300, 400))


cv2.imshow('result', result)

cv2.waitKey(0)
cv2.destroyAllWindows()