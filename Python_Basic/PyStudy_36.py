import cv2

'''
# 중간값 필터 적용(노이즈 제거)
org = cv2.imread('./Python_Basic/image/salt_pepper.png')
median = cv2.medianBlur(org, 5)

cv2.imshow('original', org)
cv2.imshow('median', median)    # 노이즈 제거! 중값값 활용

cv2.imwrite('./Python_Basic/image/median_salt_pepper.png', median)

cv2.waitKey(0)
'''

# 각종 필터 사용 비교
org = cv2.imread('./Python_Basic/image/mandrill.png')
gaussian = cv2.GaussianBlur(org, (9,9), 1)
median = cv2.medianBlur(org, 9)
bilateral = cv2.bilateralFilter(org, 9, 50, 50) # 양방향 필터

cv2.imshow('original', org)
cv2.imshow('gaussian', gaussian)
cv2.imshow('median', median)
cv2.imshow('bilateral', bilateral)

cv2.waitKey(0)