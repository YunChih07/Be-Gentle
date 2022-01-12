import speech_recognition as sr
import pygameimport speech_recognition as sr
import pygame
import time
import RPi.GPIO as GPIO
from datetime import date
from gpiozero import LED
from time import sleep

red = LED(17)
relay1 = LED(14)
relay2 = LED(15)

#channel = 21

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)


#record
r = sr.Recognizer()
mic = sr.Microphone()

print("hello")

while True:
    with mic as source:
        audio = r.listen(source)
    try:
        words = r.recognize_google(audio, language = 'zh-tw')
        print(words)
        if words == "結束":
            print("GoodBye")
            break
        if words == "幹":
            print("不要生氣")
            pygame.mixer.init()
            pygame.mixer.music.load('/home/pi/Music/angry.mp3')
            pygame.mixer.music.play()
            GPIO.output(21, GPIO.HIGH)
            time.sleep(30)
            pygame.mixer.music.stop()
            GPIO.output(21, GPIO.LOW)
        if words == "幹**":
            print("不要生氣")
            pygame.mixer.init()
            pygame.mixer.music.load('/home/pi/Music/angry.mp3')
            pygame.mixer.music.play()
            GPIO.output(21, GPIO.HIGH)
            time.sleep(30)
            pygame.mixer.music.stop()
            GPIO.output(21, GPIO.LOW)
        if words == "操":
            print("不要生氣")
            pygame.mixer.init()
            pygame.mixer.music.load('/home/pi/Music/angry.mp3')
            pygame.mixer.music.play()
            GPIO.output(21, GPIO.HIGH)
            time.sleep(30)
            pygame.mixer.music.stop()
            GPIO.output(21, GPIO.LOW)
        if words == "超級白":
            print("不要生氣")
            pygame.mixer.init()
            pygame.mixer.music.load('/home/pi/Music/angry.mp3')
            pygame.mixer.music.play()
            GPIO.output(21, GPIO.HIGH)
            time.sleep(30)
            pygame.mixer.music.stop()
            GPIO.output(21, GPIO.LOW)
        if words == "操**的":
            print("不要生氣")
            pygame.mixer.init()
            pygame.mixer.music.load('/home/pi/Music/angry.mp3')
            pygame.mixer.music.play()
            GPIO.output(21, GPIO.HIGH)
            time.sleep(30)
            pygame.mixer.music.stop()
            GPIO.output(21, GPIO.LOW)
        if words == "操**":
            print("不要生氣")
            pygame.mixer.init()
            pygame.mixer.music.load('/home/pi/Music/angry.mp3')
            pygame.mixer.music.play()
            GPIO.output(21, GPIO.HIGH)
            time.sleep(30)
            pygame.mixer.music.stop()
            GPIO.output(21, GPIO.LOW)
        if words == "雞*":
            print("不要生氣")
            pygame.mixer.init()
            pygame.mixer.music.load('/home/pi/Music/angry.mp3')
            pygame.mixer.music.play()
            GPIO.output(21, GPIO.HIGH)
            time.sleep(30)
            pygame.mixer.music.stop()
            GPIO.output(21, GPIO.LOW)
        if words == "主席好":
            print("主席好")
            pygame.mixer.init()
            pygame.mixer.music.load('/home/pi/Downloads/qi.mp3')
            pygame.mixer.music.play()
            GPIO.output(21, GPIO.HIGH)
            time.sleep(28)
            pygame.mixer.music.stop()
            GPIO.output(21, GPIO.LOW)
    except sr.UnknownValueError:
        print("無法翻譯")
    except sr.RequestError as e:
        print("無法翻譯")
    except KeyboardInterrupt:
        GPIO.cleanup()
