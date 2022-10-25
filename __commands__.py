import requests
import time
import speech_recognition as sr
from datetime import datetime
import webbrowser
import random
import wikipedia
from pynput.keyboard import Controller
from tkinter import *
from os import startfile
import os
from gtts import gTTS 
from playsound import playsound
from bs4 import BeautifulSoup
import __SETTINGS__

audio_book = ["https://www.youtube.com/watch?v=jxcMRkqaQdw"]

jokes = [
    "Knock knock. Who's there? Hawaii. Hawaii who? I'm fine, Hawaii you?",
    "What do you give to a sick lemon? Lemon aid!",
    "how do you kill vegetarian vampires, with a steak to the heart.",
    "What's orange and sounds like a parrot? A carrot"
]

random_joke = random.choice(jokes)
r = sr.Recognizer()

accents = __SETTINGS__.get_accent()

def speak(msg): 
    text = msg
    var = gTTS(text = text, lang = accents) 
    var.save('eng.mp3')
    playsound('.\eng.mp3')
    os.remove('.\eng.mp3')

name = __SETTINGS__.get_name()

def command_set(from_):
    run = True
    if run == True:
        #play music
        if from_ == f"{name} play music":
                speak("sure!")
                print(f"{name.capitalize()}: sure!")
                startfile(__SETTINGS__.get_song_PATH())
        
        #play cool music                  
        elif from_ == f"{name} play cool music":
            speak("sure!")
            print(f"{name.capitalize()}: sure!")
            webbrowser.open("https://www.youtube.com/watch?v=TggiPyCdpNs")
            
        #open netflix              
        elif from_ == f"{name} open netflix":
            speak("sure!")
            print(f"{name.capitalize()}: sure!")
            webbrowser.open("https://www.netflix.com/browse")
        
        #open youtube                 
        elif from_ == f"{name} open youtube":
            speak("sure!")
            print(f"{name.capitalize()}: sure!")
            webbrowser.open("https://www.youtube.com/")
        
        #open epic               
        elif from_ == f"{name} open epic":
            speak("sure!")
            print(f"{name.capitalize()}: sure!")
            webbrowser.open("https://www.getepic.com/app/my-library/favorites")
        
        #open real python                    
        elif from_ == f"{name} open real python":
            speak("sure!")
            print(f"{name.capitalize()}: sure!")
            webbrowser.open("https://realpython.com/")
        
        #what is the time                    
        elif from_ == f"{name} what is the time":
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            speak("it's "+current_time)
            print(f"{name.capitalize()}: it's"+current_time)
        
        #tell me a joke                    
        elif from_ == f"{name} tell me a joke":
            speak("sure!")
            print("Copilot: sure!")
            speak(random_joke)
            print(f"{name.capitalize()}: "+random_joke)
        
        #play audiobook                    
        elif from_ == f"{name} play audiobook":
            speak("sure")
            print(f"{name.capitalize()}: sure!")
            webbrowser.open(audio_book[0])
        
        #search wiki                   
        elif f"{name} search wiki" in from_:
                try:
                    bn = from_.replace(f"{name} search wiki", "")
                    result = wikipedia.summary(bn, sentences = 2)
                    print(result)
                    speak(result)
                except sr.UnknownValueError:
                        speak("Google Speech Recognition could not understand audio")
                        print(f"{name.capitalize()}: Google Speech Recognition could not understand audio")
                except wikipedia.exceptions.DisambiguationError:
                                speak("search not found")
                                print(f"{name.capitalize()}: search not found")
                except wikipedia.exceptions.PageError:
                                print(f"{name.capitalize()}: sorry page error")
                                speak("sorry page error")
                except wikipedia.exceptions.WikipediaException:
                                speak("search not found")
                                print(f"{name.capitalize()}: search not found")
        
        #duck search                        
        elif f"{name} duck search" in from_:
                            speak("okay")
                            s = from_.replace(f"{name} duck search ", "")
                            webbrowser.open("https://duckduckgo.com/?q=&t=chromentp&atb=v324-1")
                            Controller1 = Controller()
                            message = s,"\n"
                            time.sleep(1)
                            for msg in message:
                                time.sleep(0.2)
                                Controller1.type(msg)
        
        #weather in                       
        elif f"{name} weather in" in from_:
                            city = from_.replace(f"{name} weather in ", "")
                            url = "https://www.google.com/search?q="+"weather"+city
                            speak("okay")
                            print(f"{name.capitalize()}: okay")
                            print('Displaying Weather report for: ' + city)
                            html = requests.get(url).content
                            soup = BeautifulSoup(html, 'html.parser')
                            temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
                            speak("its "+temp)
                            print(name+": its "+temp)

        #type                    
        elif f"{name} type" in from_:
                            n = from_.replace(f"{name} type ", "")
                            time.sleep(1)
                            Controller1 = Controller()
                            message = n
                            for msg in message:
                                time.sleep(0.2)
                                Controller1.type(msg)

        #name                        
        elif from_ == f"{name}":
            speak("That's my name!")
            print(f"{name}: That's my name!")
        
        #QUIT    
        elif from_ == f"{name} quit":
            __name__=="__notmain__"
        
        #ERROR                    
        else:
                            speak("Sorry I did not understand. Try again or call SKY Co.")
                            print(f"{name.capitalize()}: Sorry I did not understand. Try again or call SKY Co.")