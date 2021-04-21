import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import pywhatkit
import webbrowser
from requests import get
import wikipedia
import pygetwindow
import sys

pygetwindow.getActiveWindowTitle()
engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
print(voice[1].id)
engine.setProperty('voices',voice[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-13)
 
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
     r = sr.Recognizer()
     with sr.Microphone() as source:
         print("Listening...")
         speak('Listening..')
         r.pause_threshold = 1
         voice = r.listen(source,timeout=1,phrase_time_limit=5)
     try:
         print("Thinking...")
         query = r.recognize_google(voice,language='en-in')
         print(f"User Said: {query}")

     except Exception as e:
         speak('Say that again please..')
         return "none"
     return query

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12:
        speak('Good Morning')
    elif hour>12 and hour >15:
        speak('Good Afternoon')
    else:
         speak('Good Evening')         

if __name__ == "__main__":
    speak('Starting Hover')
    wish()
    while True:
        query = takecommand().lower()
        if 'open notepad' in query:
            speak('Opening Notepad')
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)
        elif 'open cmd' in query or 'open command prompt' in query:
            speak('Opening CMD')
            os.system("start cmd")
        elif 'open camera'in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret,img = cap.read()
                cv2.imshow('Camera',img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cap.destroyAllWindows()
        elif 'play' in query:
              query = query.replace('play','')
              pywhatkit.playonyt(query)
        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f"your ip is {ip}")
        elif 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query,sentences=3)
            print("According to wikipedia"+results)
            speak('Accoding to wikipedia'+results)
        elif 'open youtube' in query:
             webbrowser.open('www.youtube.com')
        elif 'open stack overflow' in query:
            webbrowser.open('www.stackoverflow.com') 
        elif 'duckduckgo' in query:
            speak('what should i search duckduckgo for')
            search = takecommand()
            webbrowser.open(f'www.duckduckgo.com?q={search}')
        elif 'send message' in query:
            pywhatkit.sendwhatmsg("+918919005029","this is testing man bro",16,21)
        elif 'security camera' in query or 'i amm going out' in query:
             cam = cv2.VideoCapture(0)
             while cam.isOpened():
                 ret,frame = cam.read()
                 if cv2.waitKey(10) == ord('q'):
                     break
                 cv2.imshow('Secure cam',frame)
        elif 'i donot need anything' in query:
            speak("thanks")
            sys.exit()
        elif 'shutdown' in query or 'shut down' in query:
             speak('Shutting Down Windows')
             os.system("shutdown /s /t 00")
        else:
            speak('i donot know that')     