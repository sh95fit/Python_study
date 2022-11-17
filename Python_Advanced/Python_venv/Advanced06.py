# 함수 중금
'''
다양한 매개변수(*arg, **kwargs)

위치 매개변수(positional parameter)
- 가장 기본적인 매개변수
- 함수를 호출할 때 순서대로 데이터(인자)를 넘겨줘야 한다.
- 다른 매개변수와 함께 쓸 때는 항상 맨 앞에 써야한다.

ex> 함수 정의
  def my_func(a,b)
    print(a,b)

ex> 함수 호출
  my_func(a,b)

기본 매개변수(default parameter)
- 매개변수의 기본적인(default) 값
- 함수를 정의할 때 매개변수의 기본 값을 지정할 수 있다.

ex> 함수 정의
  def post_info(title, content='내용없음') :
    print("제목 : ", title)
    print("내용 : ", content)

ex> 함수 호출 - 매개변수가 일부 없는 경우 
  post_info('제목')

출력
-> 제목 : 제목
-> 내용 : 내용없음


키워드 매개변수(keyword parameter)
- 함수 호출 시 키워드를 붙여 호출한다.
- 매개변수의 순서를 지키지 않아도 된다.

ex> 함수 정의 
  def post_info(title, content) :
    print("제목 : ", title)
    print("내용 : ", content)

ex> 함수 호출
  post_info(content="내용", title="제목")

출력
-> 제목 : 제목
-> 내용 : 내용


위치 가변 매개변수(positional variable length parameter)
가변 매개변수 = 개수가 정해지지 않은 매개변수
매개변수 앞에 *가 붙는다. (튜플형태로 받아옴!)

ex> 함수 정의
    def print_fruits(&args)
        for arg in args :
            print(arg)

ex> 함수 호출
    print_fruits('apple', 'orange', 'mango')

출력
-> apple
-> orange
-> mango


키워드 가변 매개변수(keyword variable length parameter)
가변 매개변수 = 개수가 정해지지 않은 매개변수
매개변수 앞에 **가 붙는다. (딕셔너리형)

ex> 함수 정의
    def comment_info(**kwargs):
        for key, value in kwargs.items()
            print(f'{key} : {value}')

ex> 함수 호출
    comment_info(name='이름', content='내용')

출력
-> name : 이름
-> content : 내용

#매개변수 작성 순서!
위치 -기본 - 위치 가변 - 키워드(기본) - 키워드 가변
'''

# 위치 매개변수

def my_func(a, b) :
    print(a, b)

my_func(2, 3)


# 기본 매개변수

def post_info(title, content='내용없음') :
    print("제목 : ", title)
    print("내용 : ", content)

post_info(1)


# 키워드 매개변수

def post_info(title, content='내용없음') :
    print("제목 : ", title)
    print("내용", content)

post_info(content= "내용", title= "제목")


# 위치 가변 매개변수
def print_fruits(*args):  # 튜플 형태!
    for arg in args :
        print(arg)

print_fruits('apple', 'orange', 'mango', 'grape')

# 키워드 가변 매개변수
def comment_info(**kwargs) :  #딕셔너리 형태!!
    print(kwargs)
    for key, value in kwargs.items() :
        print(f"{key} : {value}")

comment_info(name="이름", content="내용")


#매개변수 작성 순서!
#위치 -기본 - 위치 가변 - 키워드(기본) - 키워드 가변

def para_info(title, content, *args) :   #가변 매개변수가 앞에 있으면 범위를 확인할 수 없으므로 에러 발생!
    pass
# 순서 상관 없이 쓰고 싶은 경우 - 호출에서 조치!(키워드 매개변수로 바꿔줌)
def para_none_info(*args, title, content) :
    pass
para_none_info('데이터1', '데이터2', '데이터3', title='데이터4', content='데이터5')

# 키워드 가변 매개변수도 반영할 경우
def para_key_info(*args, title, content, **kwargs) :  # 키보드 가변 매개변수 뒤에는 어떠한 매개변수도 올 수 없다!
    pass
