import speech_recognition as s_r
import pyttsx3
import datetime
import subprocess
import pyaudio
from selenium import webdriver
import pywhatkit
mic = s_r.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


talk('Hey, I am Ace assistant. What should I do for you?')


def content():
    with s_r.Microphone() as source:
        print('Listening!!!')
        command = mic.listen(source)
    try:
        print('Recognizing...')
        request = mic.recognize_google(command, language='en-in')
    except Exception as e:
        return "None"

    return request


def run_ace():
        command = content()
        if ('hello' in command) or ('hi' in command):
            talk('Hello there! My name is Ace. How may I help you.')
            print('Hello there! My name is Ace. How may I help you.')
        if 'time' in command:
            cur_time = datetime.datetime.now().strftime('%I:%M %p')
            print(cur_time)
            talk(cur_time)
        if 'weather' in command:
            talk('getting the latest weather report for your area.')
            print('Getting the latest weather report for your area.')
            driver = webdriver.Chrome('C://Users//shant//OneDrive//Desktop//chromedriver_win32 (1)//chromedriver.exe')
            driver.get('https://weather.com/en-IN/weather/tenday/l/Lonavala+India+INXX0367:1:IN')
            driver.refresh()
        if ('Google' in command) or ('Chrome' in command) or ('Google Chrome' in command):
            talk('opening Google Chrome')
            print('opening Google Chrome')
            subprocess.Popen('C://Program Files//Google//Chrome//Application//chrome.exe')
        if'Whatsapp' in command:
            talk('opening whatsapp')
            print('opening whatsapp')
            subprocess.Popen('C://Users/shant/AppData/Local/WhatsApp/WhatsApp.exe')
        if ('edge' in command) or ('internet explorer' in command) or ('Microsoft Edge' in command):
            talk('opening Edge')
            print('opening Edge')
            subprocess.Popen('C://Program Files (x86)//Microsoft//Edge//Application//msedge.exe')
        if 'search for' in command:
            talk('search results are on there way')
            print('search results are on there way')
            command = command.replace('search for', '')
            command = command.replace(' ', '')
            driver = webdriver.Chrome('C://Users//shant//OneDrive//Desktop//chromedriver_win32 (1)//chromedriver.exe')
            driver.get('http://www.' + command)
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        if ('power off' in command) or ('sleep' in command):
            talk('Thanks for having me. Hope to see you soon')
            print('Thanks for having me. Hope to see you soon!!!')
            exit()


while True:
    run_ace()

