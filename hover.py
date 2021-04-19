import pyttsx3, os,sys,pywhatkit,datetime,keyboard,smtplib,youtube_dl,math,subprocess,wikipedia,winsound,pyaudio
import speech_recognition as sr 
import webbrowser as web
# The text to speech voice modification
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
#variables
hour = int(datetime.datetime.now().hour)
listener = sr.Recognizer()
#This Speak Function will make the system speak
def speak(text):
    engine.say(text)
    engine.runAndWait()
# Wishme Function wishes you Good Morning Good Afternoon  Good Evening or good Nigth
def wishMe():
    if hour <=0 & hour > 12:
        speak("Good Morning SaiSaaketh")
    elif hour > 12 & hour < 15:
        speak("Good Afternon Saaketh")
    elif hour > 9 & hour < 15:
         speak("Good Evening Saaketh")
    else:
         speak("Good Night Saaketh")
#listentouser function will listen to the user and recognize the spoken words speech Synthesis         
def listentouser():
    with sr.Microphone() as source:
        speak('Listening...')
        print('listening...')
        voice = listener.listen(source)
        command = " "
    try:
        command = listener.recognize_google(voice)
        command = command.lower()
        print(command)
        speak('Thinking...')
        print('Thinking...')
        if 'hover' in command:
            command = command.replace('hover', '')
            print(command)
            print('Thinking...')
    except:
        pass
    return command
#getcommand function is used to recognize spoked words but this time i'm using this function to use the wake word which is in function line  83
def getcommand():
    command = " "
    try:
        with sr.Microphone() as source:
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
    except:
        pass
    return command
#Execution function is used to do a particular task given by the user if task or the skill is coded
def Execution():
    #Note:the code below the lines from 60 to 81 can be edited. In case you want to make your own skill and the other part of the code should not be edited
         command = listentouser().lower()
         if 'wikipedia' in command:
             command = command.replace('wikipedia','')
             results = wikipedia.summary(command)
             print("Saaketh Said:",command)
             print(results)
             speak(results)
         elif 'play' in command:
             print("Saaketh Said:",command)
             print("Hover Said: Playing",command)
             command = command.replace('play','')
             speak("playing"+command)
             pywhatkit.playonyt(command)
         elif 'open' and 'on brave' in command:
             bravepath = "C://Program Files//BraveSoftware//Application//brave.exe"          
             web.get(bravepath).open('https://google.com') 
         elif 'shutdown' in command:
              a = int(input("after how much time:"))
              pywhatkit.shutdown(time=a)
              if 'cancel shutdown' in command:
                  pywhatkit.cancelShutdown()
         elif 'i donot need anything' in command or 'bye' in command:
             sys.exit()
         else:
              speak('I donot know that') 
#wakeword function is used to wake the assistant using the word              
def wakeword():
            wishMe()    
            while True:
                command = getcommand()
                if 'friday' in command:
                    Execution()
                elif 'shut up' in command or 'goodbye' in command:
                    sys.exit()
                else:
                  hoverbusy = "no"        