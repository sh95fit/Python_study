# 자주 나는 오류 정리

# site loading 기다리기
'''
사이트 로딩 기다리기의 필요성
- 사이트에 원하는 데이터, 버튼이 존재하지 않을 수 있다.

기본적인 사이트 로딩 기다리기
selenium에서 기본적으로 기다려주는 항목
- HTTP Response 및 Rendering(javascript의 일부(event에 의해 실행되는 영역은 기다려주지 않음))을 기다림

- selenium에서 기본적으로 기다려주지 않는 항목에 대해 로딩을 기다리게 하는 명령어
 title_is   
 title_contains
 presence_of_element_located
 visibility_of_element_located
 visibility_of
 presence_of_all_elements_located
 text_to_be_present_in_element              // 비동기 데이터의 경우 데이터가 없더라도 element는 존재할 수 있다 / 이런 상황에서 사용!
 text_to_be_presnet-in_element_value        // text는 그 안에 값이 있는 경우 반환하므로 비동기 데이터 처리 시 보다 안전함!
 frame_to_be_available_and_switch_to_it     // 프레임이 생겼다 없어졌다 반복되는 경우 프레임이 존재하면서 사용이 가능할 때까지 기다렸다 사용 가능한 경우 연결
 invisibility_of_element_located
 element_to_be_clickable                    // 클릭이 가능해질 때까지 기다림 (ex> 동의 체크를 하지 않으면 버튼이 활성화되지 않음!)
 staleness_of
 element_to_be_selected
 element_located_to_be_selected
 element_selection_state_to_be
 element_located_selection_state_to_be
 alert_is_present                           // 경고창을 기다림
'''

# screenshot 찍기
