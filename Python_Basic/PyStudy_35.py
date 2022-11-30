# OpenCV 기초

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

'''
# matplotlib로 이미지 출력하기
img = mpimg.imread('./Python_Basic/image/book.png')

# 0 : 검정색, 1 : 흰색   // 색상 0~255 사이 값으로 RGB 색상이 결정된다
# 비트맵 : 이미지를 잘게 쪼갠 범위
#print(img)  # 이미지가 아닌 숫자값을 가져온다!

img_plt = plt.imshow(img)
plt.show()
'''

import cv2 

'''
# 회색, 컬러 이미지 출력하기
img_gray = cv2.imread('./Python_Basic/image/mandrill.png', cv2.IMREAD_GRAYSCALE) # 이미지를 회색으로 불러옴
img_color = cv2.imread('./Python_Basic/image/mandrill.png', cv2.IMREAD_COLOR)   # 이미지를 컬러로 불러옴

cv2.imshow('grayscale', img_gray)
cv2.imshow('colorimage', img_color)

cv2.waitKey(0)  # 사용자 입력을 기다림 
'''

# 이미지 위에 라인 그리기
'''
# 이미지 좌표는 좌측 상단이 0,0이다
# cv2.line(이미지, 시작지점좌표, 종료지점좌표, 색상, 굵기, 선의종류, 좌표시프트)


img = cv2.imread('./Python_Basic/image/mandrill.png')
cv2.line(img, (0,0), (200,200), (255,255,255), 10)  # 라인 그리기
cv2.arrowedLine(img, (0,255), (200,20), (0,255,0), 5)  # 화살표가 표시되는 라인 그리기
cv2.rectangle(img, (0,200), (200,20), (0,0,0), 5)
cv2.putText(img, "Test", (50,70), fontFace=7, fontScale=4, thickness=3, color=(0,0,0))  # (이미지, 입력할 텍스트, 위치, 폰트종류, 폰트크기, 폰트굵기, 폰트색상)
cv2.imshow('lined', img)

cv2.waitKey(0)
'''

'''
# 첫번째 이미지와 두번째 이미지 합성하기 (투영도 활용)
global img1, img2  

def on_change_weight(x) :   # 가중치
    weight = x/100
    img_merged = cv2.addWeighted(img1, 1-weight, img2, weight, 0) #(첫번째 이미지, 투영도 최대 1 - 가중치, 두번째 이미지, 가중치, 호출된 함수(자기 자신인 경우 0!))
    cv2.imshow("Display", img_merged)

img1 = cv2.imread('./Python_Basic/image/green_back.png')
img2 = cv2.imread('./Python_Basic/image/iceberg.png')

img1 = cv2.resize(img1, (300,400))
img2 = cv2.resize(img2, (300,400))

cv2.namedWindow('Display')  # 윈도우 창을 만듦
cv2.createTrackbar('weight', 'Display', 0, 100, on_change_weight) # 좌우로 움직이는 트랙바를 만듦 (트랙바가 지칭하는 것, 트랙바가 포함되는 곳, 최소값, 최대값, 호출할 함수)

cv2.waitKey(0)
'''

'''
# 이미지를 마스크로 합성하기
mask_img = cv2.imread('./Python_Basic/image/mask_circle.png')
back_img = cv2.imread('./Python_Basic/image/iceberg.png')

mask_img = cv2.resize(mask_img, (300,400))
back_img = cv2.resize(back_img, (300,400))

mask_and = cv2.bitwise_and(mask_img, back_img)    # 비트 and 연산(둘다 1인 경우만 1)
mask_or = cv2.bitwise_or(mask_img, back_img)
mask_xor = cv2.bitwise_xor(mask_img, back_img)

cv2.imshow('mask', mask_img)
cv2.imshow('back', back_img)
cv2.imshow('and', mask_and) 
cv2.imshow('or', mask_or)
cv2.imshow('xor', mask_xor)

cv2.waitKey(0)
'''

'''
# numpy를 이용해 주위 평균값으로 흐림 처리하기
import numpy as np

org = cv2.imread('./Python_Basic/image/mandrill.png')

kernel1 = np.ones((3,3), np.float32) / 9    #주변 8개의 픽셀과의 평균을 구해 해당 색상을 취함
kernel2 = np.ones((9,9), np.float32) / 81   #주변 80개의 픽셀과의 평균을 구해 해당 색상을 취함

averaged33 = cv2.filter2D(org, -1, kernel1) 
averaged99 = cv2.filter2D(org, -1, kernel2)

cv2.imshow('original', org)
cv2.imshow('filter1', averaged33)
cv2.imshow('filter2', averaged99)

cv2.waitKey(0)
'''

'''
# 가우시안으로 흐림처리하기
org = cv2.imread('./Python_Basic/image/mandrill.png')

averaged33 = cv2.GaussianBlur(org, (3,3), 1)
averaged99 = cv2.GaussianBlur(org, (9,9), 2)    # (이미지, 영역사이즈, 값) : 값이 높을수록 흐림처리가 커진다

cv2.imshow('original', org)
cv2.imshow('filter1', averaged33)
cv2.imshow('filter2', averaged99)

cv2.waitKey(0)
'''