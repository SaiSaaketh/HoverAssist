import os,sys,pywhatkit,datetime,keyboard,smtplib,youtube_dl,math,subprocess,wikipedia,winsound,pyaudio
import webbrowser as web
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
hour = int(datetime.datetime.now().hour)

def speak(text):
    engine.say(text)
    engine.runAndWait()
def wishMe():
    if hour <=0 & hour > 12:
        speak("Good Morning SaiSaaketh")
    elif hour > 12 & hour < 15:
        speak("Good Afternon Saaketh")
    else:
         speak("Good Evening Saaketh")
def ytdl():
    speak("What Do you wanna download")
    speak('a channel or a video or a playlists')
    if 'channel' in query:
        speak('which channel do you wanna download')
def classify():
    command = input("what do yo wanna do")
    if 'wikipedia' in command:
             command = command.replace('wikipedia','')
             results = wikipedia.summary(command)
             print("Saaketh Said:",command)
             print("Hover Said:",results)
             print(results)
             speak(results)
    elif 'play' in command:
             print("Saaketh Said:",command)
             print("Hover Said: Playing",command)
             command = command.replace('play','')
             speak("playing the song" )
             pywhatkit.playonyt(command)
    elif 'shutdown' in command:
        speak("shutting down")
        pywhatkit.shutdown()
while True:
    speak('Initializing Hover')
    wishMe()
    classify()                
