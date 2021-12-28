# 이미지 임계처리
# 스레시홀딩은 바이너리 이미지를 만드는 가장 대표적인 방법입니다. 
# 바이너리 이미지(binary image)란 검은색과 흰색만으로 표현한 이미지를 의미합니다. 
# 스레시홀딩이란 여러 값을 어떤 임계점을 기준으로 두 가지 부류로 나누는 방법을 의미합니다.
# https://webnautes.tistory.com/1257

import cv2
image = cv2.imread('data/images/truth.png')

# 구분 값을 먼저 설정
thresh = 255
# 위의 특정 값보다 큰 값들은 모두 255로 변경
maxValue = 255

cv2.imshow('Original', image)

# 쓰레숄딩 적용된 이미지
# dst가 이미지
th, dst = cv2.threshold(src = image, thresh=thresh, maxval=maxValue, type = cv2.THRESH_BINARY)
cv2.imshow('thresholded image', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()