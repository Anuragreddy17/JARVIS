import speech_recognition as sr
import webbrowser
import os
import time
import pyttsx3

engine = pyttsx3.init()
rate = engine.getProperty('rate');
engine.setProperty('rate',130);
r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)
try:
    print(r.recognize_google(audio))
    X = r.recognize_google(audio)
except sr.UnknownValueError:
    print("if you said something i couldn't hear what it waas!")
    X = "try again"  
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

#if X == 'open the door' :
    
    #webbrowser.open('http:192.168.43.34/toggle1')
    
#if X == 'light on' :
 #   
  #  webbrowser.open('http:192.168.43.34/toggle2')
   # time.sleep(3)
    #webbrowser.open('http:192.168.43.34/toggle2')
    

if X == 'close the door' :
    
    webbrowser.open('http:192.168.43.34/toggle1')
    time.sleep(3)
    webbrowser.open('http:192.168.43.34/toggle1')
    
#else :
 #   print("Error")
 
if X == 'close the door' :
    engine.say('The Door is closing')
    engine.runAndWait()

if X == 'light on' :
    webbrowser.open('http:192.168.43.34/toggle2')

if X == 'light off' :
    webbrowser.open('http:192.168.43.34/toggle2')
