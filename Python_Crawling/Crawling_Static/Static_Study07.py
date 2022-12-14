# CSS Selector - html tag, id, class, attribute, 한정자, 고급한정자
'''
HTML Element Type을 구분하여 크롤링
a, div, span 등 태그 혹은 id를 기준으로 서칭
구분자 : .(class) #(id) [](attribute) :(고급한정자)

Tip! css selector 테스트 방법
크롬 개발자 도구 활용
document.querySelector()    : 서칭된 것 중 가장 첫번째 요소만 가져옴
document.querySelectorAll() : 서칭된 요소들을 모두 가져옴

id
id는 class와 다르게 유일한 값을 가진다!(예외의 경우 2개 이상이 쓰일 경우도 존재)
특정 Element의 유일성을 보장할 때 주로 활용
#을 이용해 id를 가져올 수 있음

class
id와 다르게 여러 요소에 동일한 값을 가질 수 있다
따라서 공통된 디자인이 필요한 HTML Element들에 모두 들어가 있다!
즉, HTML Element의 그룹을 의미한다

attribute
id, class 또한 attribute의 일종
attribute는 속성을 의미 -> 특별한 값을 부여함
ex> alt, checked, data, href, id 등
*= : 포함
^= : ~으로 시작
$= : ~으로 끝남
활용 예시
태그[속성*='값'] : 속성 내에 값이 포함되는 것들을 찾음

한정자
한정자 = selector
좀 더 세밀하게 select를 하고 싶을 때 사용
ex>
*       : 모든 노드들
div,p   : div와 p 노드들
div p   : div 안에 있는 p 노드들
div>p   : div 바로 안에 있는 p 노드들
div~p   : p 옆(앞)에 있는 div 노드들
div+p   : div 옆(뒤)에 있는 p 노드들

고급 한정자
일반 한정자에서 더 세밀하게 select가 가능하다
ex>
:enabled    - 활성화된 상태
:checked    - 체크된 상태
:disabled   - 비활성화된 상태
:empty      - 값이 비어있는 상태
:first-child    - 첫번째 자식
:last-child     - 마지막 자식
:first-of-type  - 해당 타입의 첫번째 노드
:last-of-type   - 해당 타입의 마지막 노드
:hover          - 마우스가 올라갔을 때
:not            - 다음 조건이 거짓인 경우
:nth-child      - n번째 자식
:nth-of-type    - n번째 타입

'''

from bs4 import BeautifulSoup as BS
# module 'collections' has no attribute 'Callable' 에러 대응
# collections.Callable 참조가 파이썬 3.10부터 collections.abc.Callable로 이동하여, 제거된 Attribute라서 발생하는 오류
import collections     
if not hasattr(collections, 'Callable'):
    collections.Callable = collections.abc.Callable
#------------------------------------------------------------------


# BS 적용 테스트
# * Tip! multi line string : """ 줄이 바껴도 주석이 풀리지 않음 """
html = """
<html>
    <body>
        <div>안녕하세요</div>
    </body>
</html>
"""

soup = BS(html, "html.parser")

div = soup.select("div")
print(div[0].get_text(strip=True))