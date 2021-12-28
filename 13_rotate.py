import cv2
image = cv2.imread('data/images/sample.jpg')
print(image.shape)
cv2.imshow('Original', image)

# 회전시킬 이미지를 만들기 위한 정보 셋팅
# center = (x축, y축) 변수 : 중심 지정
center = (image.shape[1] / 2, image.shape[0] / 2)
rotationAngle = 30
scaleFactor = 1

matrix = cv2.getRotationMatrix2D(center = center, angle = rotationAngle, scale = scaleFactor)
print(matrix)
result = cv2.warpAffine(src = image, M = matrix, dsize=(image.shape[1], image.shape[0]))
cv2.imshow('ratationAngle', result)
cv2.waitKey(0)
cv2.destroyAllWindows()