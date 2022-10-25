#
#beta
#copilot 0.2
import requests
import time
import pyttsx3
import speech_recognition as sr
from datetime import datetime
import webbrowser
import random
import wikipedia
from pynput.keyboard import Controller
from tkinter import *
import os
from gtts import gTTS 
from playsound import playsound

debug = False
running = True

name = ""

audio_book = ["https://www.youtube.com/watch?v=jxcMRkqaQdw"]

jokes = [
    "Knock knock. Who's there? Hawaii. Hawaii who? I'm fine, Hawaii you?",
    "What do you give to a sick lemon? Lemon aid!",
    "how do you kill vegetarian vampires, with a steak to the heart.",
    "What's orange and sounds like a parrot? A carrot"
]

random_joke = random.choice(jokes)
gender = 1
r = sr.Recognizer()
engine = pyttsx3.init()

#settings
accents = "ja" #accents ja for japenese, hi for hindi, com.au for australian, co.in for indian, fr for french, and en for english

def speak(msg): 
    text = msg
    var = gTTS(text = text, lang = accents) 
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

            if "hey copilot" in comand:
                speak("Yes")
                print("Copilot: Yes")
                print("did you say: "+comand)
                
            elif comand == "copilot play music":
                speak("sure!")
                print("Copilot: sure!")
                webbrowser.open("https://www.youtube.com/watch?v=bJpL9AT7mTA&t=980s")
                
            elif comand == "copilot play cool music":
                speak("sure!")
                print("Copilot: sure!")
                webbrowser.open("https://www.youtube.com/watch?v=TggiPyCdpNs")
                
            elif comand == "copilot open netflix":
                speak("sure!")
                print("Copilot: sure!")
                webbrowser.open("https://www.netflix.com/browse")
                
            elif comand == "copilot open youtube":
                speak("sure!")
                print("Copilot: sure!")
                webbrowser.open("https://www.youtube.com/")
                
            elif comand == "copilot open epic":
                speak("sure!")
                print("Copilot: sure!")
                webbrowser.open("https://www.getepic.com/app/my-library/favorites")
                
            elif comand == "copilot open real python":
                speak("sure!")
                print("Copilot: sure!")
                webbrowser.open("https://realpython.com/")
                
            elif comand == "copilot what is the time":
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                speak("it's "+current_time)
                print("Copilot: it's"+current_time)
                
            elif comand == "copilot tell me a joke":
                speak("sure!")
                print("Copilot: sure!")
                speak(random_joke)
                print("Copilot: "+random_joke)
                
            elif comand == "copilot play audiobook":
                speak("sure")
                print("Copilot: sure!")
                webbrowser.open(audio_book[0])
                
            elif "search" in comand:
                try:
                    bn = comand.replace("search ", "")
                    result = wikipedia.summary(bn, sentences = 2)
                    print(result)
                    speak(result)
                except sr.UnknownValueError:
                    speak("Google Speech Recognition could not understand audio")
                    print("Copilot: Google Speech Recognition could not understand audio")
                except wikipedia.exceptions.DisambiguationError:
                    speak("search not found")
                    print("Copilot: search not found")
                except wikipedia.exceptions.PageError:
                    print("Copilot: sorry page error")
                    speak("sorry page error")
                except wikipedia.exceptions.WikipediaException:
                    speak("search not found")
                    print("Copilot: search not found")
                    
            elif "duckduckgo lookup" in comand:
                speak("okay")
                s = comand.replace("duckduckgo look up ", "")
                webbrowser.open("https://duckduckgo.com/?q=&t=chromentp&atb=v324-1")
                Controller1 = Controller()
                message = s,"\n"
                time.sleep(1)
                for msg in message:
                    time.sleep(0.2)
                    Controller1.type(msg)
                    
            elif "weather in" in comand:
                e = comand.replace("weather in ", "")
                speak("okay")
                print("Copilot: okay")
                print('Displaying Weather report for: ' + e)
                url = 'https://wttr.in/{}'.format(e)
                res = requests.get(url)
                print(res.text)
                
            elif "type" in comand:
                n = comand.replace("type ", "")
                time.sleep(1)
                Controller1 = Controller()
                message = n
                for msg in message:
                    time.sleep(0.2)
                    Controller1.type(msg)
                
            else:
                speak("Sorry I did not understand")
                print("Copilot: Sorry I did not understand")
            
    except:
        pass
    
    
#start
speak("x")
speak("wellcome Sky Solas") # Sky is my nickname
print("Copilot: wellcome Sky Solas")
speak("what can I do for you")
print("Copilot: what can I do for you")

#loop
while running == True:
    time.sleep(1)
    take_command()