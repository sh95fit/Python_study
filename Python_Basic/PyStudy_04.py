# 파일 다루기
'''
파일 입력/출력 함수
1. open()
2. write()

파일 객체 = open(파일명, 열기모드) //r(읽기 전용), w(쓰기), a(추가, 쓰기한 것들이 반영)
'''


# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape

# \가 유니코드로 인식되서 발생하는 문제  -> / 혹은 \\로 대체

# 에러가 발생하는 문장
# f = open("C:\Users\tpgns\Desktop\Python_Study\test.txt", 'w')
# f.close()


# 대안
f = open("C:/Users/tpgns/Desktop/Python_Study/Python_Basic/test.txt", 'w')  # \를 /로 변경
f.write("test")
f.close()
