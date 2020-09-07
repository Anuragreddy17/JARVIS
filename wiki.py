import wikipedia
import pyttsx3
import speech_recognition as sr
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',130)
print ('J.A.R.V.I.S')
r = sr.Recognizer()
with sr.Microphone() as source:
    engine.say('What do you wanna know about')
    engine.runAndWait()
    audio = r.listen(source)
try:
    print(r.recognize_google(audio))
    X = r.recognize_google(audio)
except sr.UnknownValueError:
    print("if you said something i couldn't hear what it waas!")
    X = "try again"  
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
w = wikipedia.page(X)
engine.say(w.summary)
engine.runAndWait()
