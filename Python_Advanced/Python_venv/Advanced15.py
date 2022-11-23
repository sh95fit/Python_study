# 정규표현식
'''
문자열 추출 - 문자열에서 특정 패턴(전화번호, 이메일 형식 등)을 찾을 경우 유용하게 사용
유효성 검사 - if 조건으로 지정하기엔 복잡하므로 정규표현식 사용

정규 표현식의 장점
- 문자열 추출, 유효성 검사에서 유용하게 쓰일 수 있다
- 거의 모든 언어에서 지원하므로 범용성이 높다

정규 표현식의 단점
- 가독성이 좋지 못하다
- 유지보수가 힘들다

정규 표현식 사용 방법
- Flags 
 정규 표현식을 찾아주는 옵션

- Character classes
  .  : 모든 문자를 뜻함
  \w : alphanumeric & underscore  (알파벳, 숫자 & 언더바(_))
  \d : digit 숫자
  \s : whitespace
  \W \D \S : not word, digit, whitespace (\w와 반대) 
  [abc] : a,b,c에 해당하는 모든 단어 추출 ([] 안은 수정 가능)
  [^abc] : not a, b, c
  [a-g] : character between a & g  즉 a~g 사이 문자를 찾을 때
  [가-힣] : 모든 한글을 찾을 때
  

- Anchors
  ^abc$ :   ^abc - 문장의 시작 부분 (start) (즉, abc로 시작하는 모든 단어 추출)  / abc$ - 문장의 끝 부분 (end of the string) (즉, abc로 끝나는 모든 단어 추출)
  \b \B :  \b를 앞에 쓰는 경우 - 단어의 앞부분에 해당되는 단어 추출 / 뒤에 쓰는 경우 - 단어의 끝부분에 해당되는 단어 추출
           \B를 앞에 쓰는 경우 - 단어의 앞부분이 아닌 단어 추출 / 뒤에 쓰는 경우 - 단어의 끝부분이 아닌 단어 추출
  #중요! multiline 지정 시 한줄씩 처리해서 Anchors 적용 가능 / 미지정 시 전체를 하나의 범위로 처리하므로 찾을 수 없음


- Escaped Characters
  \. : 마침표 문자 자체를 찾을 경우
  \* : 별표를 찾을 경우
  \\ : \를 찾을 경우
  \t, \n, \r : Tab(탭), Linefeed(줄바꿈), carriage return


- Quantifiers & Alternation 
  a* : 0 or more (0개 또는 그 이상)
  a+ : 1 or more (1개 또는 그 이상)
  a? : 0 or 1 (0개 또는 1개)
  a{5} : exactly five (a가 정확하게 5개가 유효한 단어 추출)
  a{2,} : 2 or more (a가 2개 또는 그 이상)
  a{1,3} : between 1 and 3 (a개 1개~ 3개 사이인 단어 추출)
  a.+, : greedy 방식으로 매치가 되는 만큼 계속 진행
  a.+?. : 매치가 최소한으로 일어나는 경우로 추출
  #.{3,}?,: 3글자 이상인 값 추출
  ab|cd  : match ab or cd (ab 또는 cd를 포함하는 단어 추출 ) (즉, 둘다 추출하고 싶은 경우)


- Group & Lookaround
  gr(e|a)y : grey, gray 둘 다 찾음   (=다른 방법 gr[ae]y)
  그룹으로 가져온 뒤 불필요한 부분을 제거할 때!
  #(.+?), : #과 ,를 제외한 필요한 부분만 추출
  즉 그룹은 특정 필요한 부분만 뽑아내거나 or 연산을 사용할 때 자주 사용
  \1 : backreference to group #1 (역참조) (앞에서 사용한 그룹을 뒤에서 한번 더 사용)
      ex> (.+)\s\1 에서 역참조는 \1 위치에 그룹 (.+)를 한번 더 실행하는 것!  = (.+)\s(.+)
  (?:abc) : non-capturing group  그룹에서 검색조건으로만 사용되고  그룹에는 포함되지 않게 하고 싶은 경우 사용
  (?=abc) : positive lookahead   검색 조건에는 포함되나 최종 결과에는 포함되지 않게 하고 싶은 경우 사용
  (?!abc) : negative lookahead   해당값이 포함되지 않도록 하고 싶은 경우 사용



정규표현식 연습 사이트
- https://regexr.com
 Expression - 정규표현식 작성란
              ex //gm       /와 / 사이에 내용이 들어가며 gm부분에는 flags 즉 옵션을 지정한다  gm은  Flags 중 global과 multiline을 지정한 것!
                - global : 미선택 시 전체 텍스트 중 해당하는 하나의 데이터만 매칭 / 선택을 해줘야 전체 데이터 매칭
 Text - 테스트용 샘플 텍스트(임의로 지정하여 테스트 가능)
 Tools - 정규 표현식 적용 시 매칭되는데 결과값과 함께 매치가 어떻게 이루어졌는지에 대한 설명이 나타남

'''

# 파이썬 re 모듈 사용
'''
* re 모듈 메서드
match - 문자열 처음부터 검색(처음부터 맞아야 함)   (regex,문자열)   -> 찾은 경우 match object 1개 반환 / 없는 경우 None
search - 문자열의 전체를 검색(처음부터 맞지 않아도 문제 없음)   -> 찾은 경우 match object 1개 반환 / 없는 경우 None
findall - 문자열 전체 검색  -> 찾은 경우 : 문자열 리스트 / 없는 경우 : 빈 리스트
finditer - 문자열 전체 검색 -> 찾은 경우 : match object iterator / 없는 경우 : None
fullmatch - 패턴과 문자열이 남는 부분 없이 완벽하게 일치  -> 찾은 경우 : match object 1개 / 없는 경우 : None


* match 객체의 메서드
group - 매칭된 문자열 반환
start - 매칭된 문자열의 시작 위치
end - 매칭된 문자열의 끝 위치
span - 매칭된 문자열의 (시작, 끝) 튜플
'''

import re

# 1. re 모듈의 메서드

str = 'love people around you, love your work, love yourself'

# 1> match : 문자열을 처음부터 검색 (결과 : 1개의 match 객체) # 맨앞 love를 지우면 None이 나온다!
result = re.match('love', str)  
print(result)

# 2> search : 문자열의 전체를 검색 (결과 : 1개의 match 객체)
result = re.search('people', str)
print(result)

# 3> findall : 문자열의 전채를 검색 (결과 : 문자열 리스트)
result = re.findall('love', str)
print(result)

# 4> finditer : 문자열의 전체를 검색 (결과 : match 객체 이터레이터) <- 순서가 있는 자료형은 for문으로 출력하면 match object를 출력할 수 있다
result = re.finditer('love',str)
print(result)

for i in result :
    print(i)

# 5> fullmatch 패턴과 문자열이 완벽하게 일치하는지 검사
str1 = 'Hey Guys, read books'
result = re.fullmatch('Hey Guys, read books', str1)
print(result)


# 2. match object의 메서드
result = re.search('people', str)

# 1> group() : 매칭된 문자열을 반환
print(result.group())

# 2> start() : 매쳉된 그룹의 첫번째 위치 반환
print(result.start())

# 3> end() : 매칭된 문자열의 마지막 위치 반환
print(result.end())

# 4> span() : 매칭된 문자열의 (시작, 끝) 위치 튜플을 반환
print(result.span())