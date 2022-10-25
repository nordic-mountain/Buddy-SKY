#
#beta
#copilot 0.2
import time
import pyttsx3
import speech_recognition as sr
import os
from gtts import gTTS 
from playsound import playsound
import __commands__
import __SETTINGS__

running = True

name = __SETTINGS__.get_name() 

r = sr.Recognizer()
engine = pyttsx3.init()

#settings
lang = __SETTINGS__.get_accent() #accents ja for japenese, hi for hindi, com.au for australian, co.in for indian, fr for french, and en for english

def speak(msg): 
    text = msg
    var = gTTS(text = text, lang = lang) 
    var.save('eng.mp3')
    playsound('.\eng.mp3')
    os.remove('.\eng.mp3')

#run
def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            audio = r.listen(source)
            reconize = r.recognize_google(audio)
            comand = reconize.lower()
            print("Your qery: "+comand)
            #commands
            __commands__.command_set(comand)
            
    except:
        pass
    
    
#start
speak("x")
speak(f"wellcome {__SETTINGS__.get_user_name()}")
print(f"{name.capitalize()}: wellcome {__SETTINGS__.get_user_name()}")
speak("what can I do for you")
print(f"{name.capitalize()}: what can I do for you")

#loop
while running == True:
    time.sleep(1)
    take_command()