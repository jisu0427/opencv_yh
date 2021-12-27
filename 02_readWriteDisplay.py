import cv2
import numpy as np

img_file = 'data/images/sample.jpg'

# opencv 로 이미지 열기(color(BGR) 로 가져오기)
image = cv2.imread(img_file, cv2.IMREAD_COLOR)

# 이미지가 정상인지 체크하는 코드
if image is None:
    print('이미지 파일을 열 수 없습니다.')
else :
    print(image.shape)

# opencv 에서는 이미지를 BGR로 읽어온다.
# 불러온 이미지를 그레이 스케일로 변경할 수 있다.
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('color',image)
cv2.imshow('gray scale',gray_image)

# 위의 imshow 함수는 화면에 표시하는 함수인데, 
# 실행되었다가, 바로 종료된다.
# cpu가 imshow를 실행 후 아래 라인을 실행하는데
# 아래 라인에 아무것도 없어 바로 프로그램이 종료된다
# 우리 눈으로 확인하기 위해서는 cpu의 코드실행을 잠시 멈추게 해야한다.
cv2.waitKey(0)
cv2.destroyAllWindows()