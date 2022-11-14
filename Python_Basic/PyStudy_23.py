# 패키지
'''
* 패키지란?
관련 있는 모듈을 하나의 폴더로 구성해 놓은 것

Tip!
폴더 표시 형태 변경 방법
ex> 상위 폴더 / 하위 폴더 형태
-> 형태를 아래와 같이 변경
    상위폴더
     하위 폴더

File -> Preferences -> Settings -> compact 검색 -> Compact Folders를 해제
'''

# 첫번째 방법 - import 패키지, 모듈
#import unit.character
#unit.character.test()

# 두번째 방법 - from 패키지 import 모듈
#from unit import item
#item.test()

# 세번째 방법 - from 패키지 import *    #(모듈 전체를 가져오는 방법! 대신 __init__ 모듈 초기 설정 필요! ex> from . import character, item, monster)
# from unit import *
# character.test()
# item.test()
# monster.test()

# 네번째 방법 - import 패키지   # 패키지를 import 할 때에도 __init__ 모듈 초기 설정 필요 ex> from . import character, item, monster
import package_test.unit
package_test.unit.character.test()
package_test.unit.item.test()
package_test.unit.monster.test()
