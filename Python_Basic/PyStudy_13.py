import tkinter     #윈도우 창을 만들어주는 라이브러리

window = tkinter.Tk()

'''
# tkinter 속성

# geometry : 가로 * 세로
# title : 창 제목
# configure : 옵션
'''

window.title("첫번째 GUI")
window.geometry('500x600+300+100')  # 가로*세로 + x좌표 + y좌표
#window.configure(background="red") # 배경색 설정
lbl = tkinter.Label(window, text="Python_Study")
lbl.pack()
txt = tkinter.Entry(window)
txt.pack()

btn = tkinter.Button(window, text='OK')
btn.pack()

window.mainloop()  #항상 소스 가장 하단에 위치시켜야 함!

