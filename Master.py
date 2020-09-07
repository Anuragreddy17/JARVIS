import os
import pyttsx3
import speech_recognition as sr
engine = pyttsx3.init()
engine.setProperty('rate', 150)
# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
 engine.say('What you want to do')
 engine.runAndWait()
 audio = r.listen(source)

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print(r.recognize_google(audio))
    X = r.recognize_google(audio)
except sr.UnknownValueError:
    engine.say("if you said something i couldn't hear what it waas!")
    engine.runAndWait()
    
elif(X == 'search'):
    os.system('wiki.py')
elif(X == 'light'or 'door'):
    os.system('Door-light.py')
elif(X == 'light'or 'door'):
    os.system('Door-light.py')
elif(X == 'master'):
    os.system('Master.py')
