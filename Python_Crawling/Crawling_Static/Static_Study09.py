# imgur 이미지 업로드하기
'''
HTTP GET vs POST
GET : 리소스 얻기
POST : 리소스 생성

Webhook.site 
- URL에 request를 보내 상태를 확인하는 용도로 활용

이미지를 HTTP(문자열)로 보내는 방법?
이미지도 문자열로 구성되어 있다!  (이미지는 RGB로 구성 (R : 0~255, G : 0~255, B : 0~255) + 추가시 불투명도)
 -> Multipart/form-data 타입 유래
  기존 Content-Type의 한계
   1. 큰 파일을 보낼 때 비효율적
   2. ASCII 문자가 아닌 것을 보낼 때 비효율적
   3. MIME를 같이 보낼 수 없음
        ex> 기존 vs multipart
        기존 예시 - HTTP Content-Type : application/x-www-form-urlencoded
        multipart - HTTP Content-Type : multipart/form-data; boundary=----WebKitFormBoundary7nBdeb5SuPhRSy3X
        (multipart 타입 : 중복을 피하기 위해 랜덤한 해시값 적용)
   기본 형태 : multipart/form-data; boundary=----WebKitFormBoundary7nBdeb5SuPhRSy3X     
   
   * 핵심 포인트 : boundary, Content-*, 빈줄 삽입
    boundary : 여러 데이터를 boundary를 통해 나눔
    Content-* : Disposition, Type 등 지정
    -> 장점 : MIME를 같이 보낼 수 있음!

imgur 사이트
- 

'''

import requests as req

# 쿼리스트링, 헤더 내용 변경해서 요청해보기
# res = req.get("https://webhook.site/3407068a-2dad-444b-91ce-32bf27f94ae3?name=hi", headers={"User-Agent" : "KIMSEHUN"})

# Webhook TEST
# url = "https://webhook.site/3407068a-2dad-444b-91ce-32bf27f94ae3"
# res = req.post(url, data={
#     "name" : "hi"
# })
# print(res.text)

url = "https://api.imgur.com/3/image?client_id=546c25a59c58ad7" # client_id는 고유 할당된 값!

# image.png
# f = open("./Python_Crawling/Crawling_Static/image.PNG", "rb")
# img = f.read()
# f.close()

# close가 번거로운 경우 아래와 같이 구성이 가능하다!
with open("./Python_Crawling/Crawling_Static/image.PNG", "rb") as f :
    img = f.read()

# 이미지 업로드 확인
# print(len(img))

# multipart/form-data 타입으로 업로드하기!
res = req.post(url, files={
    "image" : img,
    "type" : "file",
    "name" : "image.PNG"
})
print(res.status_code)
print(res.text)

# post를 통해 생성한 리소스 확인
link = res.json()["data"]["link"]
print(link)

html = f"""
    <html>
        <head>
            <title>방금 업로드한 이미지</title>
        <head>
        <body>
            <img src="{link}">
        </body>
    </html>
"""

with open("image.html", "w") as f :
    f.write(html)