# 컴퓨터 IP 주소 알아내기
'''
import socket

ip = socket.gethostbyname(socket.gethostname())

print(ip)
'''

# TTS / 텍스트를 음성으로 바꿔줌
'''
pip install gtts   / 라이브러리 설치 필요
pip install playsound / 라이브러리 설치 필요
'''

import gtts
from playsound import playsound

text = "텍스트를 음성으로 반환하기"

tts = gtts.gTTS(text=text, lang='ko')

tts.save(r"sound.mp3")
playsound(r"sound.mp3")
