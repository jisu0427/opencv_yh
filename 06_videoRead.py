import cv2
import numpy as np


# FPS : Frame per Second 1초당 몇장의 사진으로 구성되어있나?

# 비디오 파일 읽기
cap = cv2.VideoCapture('data/videos/chaplin.mp4')

if cap.isOpened() == False:
    print('비디오 파일을 여는데 실패했습니다.')
else : 
    # 동영상은 여러장의 사진으로 되어있기 때문에 반복문으로 구상한다.
    # 동영상 시작부터 끝까지 imshow를 반복해서 화면에 출력해주면 이것이 바로 동영상 플레이어이다.
    while cap.isOpened():
        # 사진 한장씩 가져온다
        ret, frame = cap.read()
        # 제대로 된 사진이면 화면에 표시
        if ret == True:
            cv2.imshow('Video', frame)
            # 동영상이 플레이하는 동안 멈추고 싶으면 esc 키를 눌러 멈추도록한다.
            if cv2.waitKey(25) & 0xff == 27:
                break
        else :
            break
    cap.release()
    cv2.destroyAllWindows()
        