# 파일 입출력 기초
'''
파일 입출력 사용 이유
파일로부터 데이터를 읽어와서 프로그램에 사용하기 위함
프로그램에서 만든 데이터를 파일 형태로 저장하기 위함

파일 열기 모드
w : 쓰기 모드(write)    # 기존에 있는 내용을 덮어쓰기
a : 추가 모드(append)   # 기존에 있는 내용에 추가로 반영(이어쓰기)
r : 읽기 모드(read)

파일 작업 절차
파일 열기 - 파일 작업 - 파일 닫기    (파일 작업 후 반드시 파일을 닫아주어야 한다!)

파일객체 = open("파일이름", "파일모드")
파일객체.write(데이터)
파일객체.close()

vs code에서는 encoding을 해주지 않으므로 설정해주어야 한다!
'''

# 1. 파일 쓰기
file = open("data.txt", "w", encoding='UTF-8')     #경로 설정이 생략된 경우 root 폴더에 생성된다!    ./하위폴더/.../data.txt 형태로 설정
file.write("1. 데이터\n")
file.close()

# 2. 파일 추가
file = open("data.txt", "a", encoding='UTF-8')
file.write("2. 데이터 추가\n")
file.close()

# 3. 파일 읽기

# 3.1. 파일 전체 읽기
file = open("data.txt", "r", encoding='UTF-8')
data = file.read()
print(data)
file.close()

# 3.2. 파일 1줄 읽기(readline())
file = open("data.txt", "r", encoding='UTF-8')
while True :
    data = file.readline()
    print(data, end="")
    if data == "" :
        break
file.close()
