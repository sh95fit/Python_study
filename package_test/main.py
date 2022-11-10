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
import unit
unit.character.test()
unit.item.test()
unit.monster.test()