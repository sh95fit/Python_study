# 데이터 타입, 문자열 조작(find, split) 기초
'''
XML, HTML, JSON 데이터 타입 살펴보기

# XML
<> ~ </> : 노드(Node)
<?  ?> : 메타 데이터 (문서 버전, 인코딩 등을 지정해주는 데이터)
가공되지 않은 데이터를 표현하은 것으로 태그에 의미가 없다!

# HTML
XML에서 조금더 발전된 규칙이 적용된 데이터
노드(Node) 내에 Tag + 메타데이터(attribute)를 통해 구분이 가능하도록 구성되어있음
태그가 정해져 있고 의미가 있음! (ex> h1~6, a, button 등)
div, span, p : 주로 텍스트 데이터를 포함한 태그

# JSON
JavaScript의 기본 데이터 타입을 활용한 데이터
파이썬의 딕셔너리 형태와 유사
구조 작성이 상대적으로 엄격함
ex>
data = {
    "title" : "제목",
    "author" : "작가"
}

Tip! json prettier : json을 깔끔한 형태로 만들어줌
     XHR : 연결 이후 추가적으로 한번더 가져온 데이터들을 지칭 (보통 JSON이 송수신된다)

'''


# 문자열 조작 파싱
'''
HTML 문서를 일반 문자열로 취급하여
원하는 문자열의 위치 등을 이용해 원하는 데이터를 추출하는 방법

find()
문자열의 위치와 길이를 기반으로 작업

split()
문자열을 배열로 쪼개내는 작업
'''

# s = 'apple'
# print(s.find('e'))
# arr = s.split('p')
# print(arr)


p = '제 생일은 3월입니다'

# 인덱스 슬라이싱을 이용한 생일 월 추출
print(p[6:8])

# find 활용
# find는 찾은 문자열의 시작 위치를 알려줌!
# find를 이용한 생일 월 추출
pos = p.find('생일은 ')   #2
pos += 4    # 4는 '생일은 '의 길이!
print(p[pos:pos+2])


# split 활용
# 길이를 모르는 경우 find보다 split이 유리!
arr = p.split('생일은 ')
print(arr[1].split('입니다')[0])
# 한 줄로 간단하게 추출 가능!
print(p.split('생일은 ')[1].split('입니다')[0])