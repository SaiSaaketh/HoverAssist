import pyttsx3, os,sys,pywhatkit,datetime,keyboard,smtplib,youtube_dl,math,subprocess,wikipedia,winsound,pyaudio,pyautogui
import speech_recognition as sr 
import webbrowser as web
# The text to speech voice modification
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('volume',1.0)
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
        listener.adjust_for_ambient_noise(source, duration=5)
        listener.pause_threshold = 1
        voice = listener.listen(source,timeout=1,phrase_time_limit=5)
        command = " "
    try:
        command = listener.recognize_google(voice,language='en-in')
        command = command.lower()
        print(command)
        speak('Thinking...')
        print('Thinking...')
    except:
        pass
    return command
#getcommand function is used to recognize spoked words but this time i'm using this function to use the wake word which is in function line  83
def getcommand():
    command = " "
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source, duration=1)
            voice = listener.listen(source,timeout=1,phrase_time_limit=5)
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
             speak("Searching wikipedia")
             command = command.replace('wikipedia','')
             results = wikipedia.summary(command)
             print("Saaketh Said:",command)
             print(results)
             speak(results)
         elif 'volume up' in command:
             pyautogui.press('F3')
         elif 'volume down'in command:
             pyautogui.press('F2')    
         elif 'play' in command:
             print("Saaketh Said:",command)
             print("Hover Said: Playing",command)
             command = command.replace('play','')
             speak("playing"+command)
             pywhatkit.playonyt(command)
         elif 'on chrome' in command:
             bravepath = "C://Program Files//BraveSoftware//Application//brave.exe"
             command=command.replace('on chrome','')
             if 'dot' in command:
                command = command.replace('dot','.')         
                web.get('chrome').open(command) 
         elif 'i donot need anything' in command or 'bye' in command:
             sys.exit()    
         elif 'shutdown' in command or 'shut down' in command:
             speak('Shutting Down Windows')
             os.system("shutdown -s 0")
         else:
              speak('I dont know that') 
#wakeword function is used to wake the assistant using the word              
def wakeword():
            speak('Starting Hover')
            wishMe()    
            while True:
                command = getcommand()
                if 'jarvis' in command:
                    Execution()
                elif 'shut up' in command or 'goodbye' in command:
                    sys.exit()
                else:
                  hoverbusy = "no" 
wakeword()                         