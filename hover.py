import datetime
import os  # os module is used to open files and run commands on the cmd and a lot of other features installation:deafult by python
import webbrowser

import pyautogui
import pyttsx3  # pyttsx3 is module for text to speech installation:pip install pyttsx3
import requests
# speechrecogntion is the module which is used for recognizing audio and converting into text installation:pip install speechrecogntion
import speech_recognition as sr

from Feature import *


def Speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1)
    engine.say(text)
    engine.runAndWait()


def getcommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print("You said: " + command + "\n")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        command = "None"
    return command


def query():
    query = getcommand()
    if query == "open notepad":
        os.system("notepad")

    if "what is the time" in query:
        min = datetime.datetime.now().strftime("%I:%M %p")
        Speak(f"It is {min}")

    elif 'browser' in query:
        Speak("opening Browser ")
        webbrowser.open("https://www.google.com")

    elif 'open cmd' in query or 'open command prompt' in query:
        Speak('Opening CMD')
        os.system("start cmd")

    elif 'ip address' in query:
        ip = requests.get('https://api.ipify.org').text
        Speak(f"your ip is {ip}")

    elif 'wikipedia' in query:
        Speak('Searching Wikipedia')
        import wikipedia
        query = query.replace('wikipedia', '')
        results = wikipedia.summary(query, sentences=3)
        Speak('Accoding to wikipedia'+results)

    elif 'search' in query:
        Speak("Searching The Internet")
        search = query.replace("search", "")
        webbrowser.open(f'www.google.com/search?q={search}')

    elif 'i am going' in query:
        Speak(
            "ok i will open ..security camera. to secure your device")
        Security_Cam()

    elif 'open' in query.lower():
        query = query.replace("open", "")
        query = query.replace("chrome", "")
        Speak(f"Opening {query} ")
        Webopener(query=query)

    elif "weather" in query:
        from Feature import Weather
        w = Weather()
        Speak(w)

    elif 'shutdown' in query or 'shut down' in query:
        Speak('Shutting Down Windows')
        os.system("shutdown /s /t 00")

    elif 'switch the window' in query:
        Speak("I'll switch the window for you")
        pyautogui.hotkey("Alt", "Tab")

    elif 'take a screenshot' in query:
        Speak("taking screenshot buddy")
        pyautogui.hotkey("Win", "prtsc")

    elif "volume up" in query:
        Speak("Turning the volume up")
        pyautogui.press("volumeup")

    elif "speed test" in query or "speedtest" in query:
        SpeedTest(query=query)

    elif "volume down" in query:
        Speak("Turning the volume down")
        pyautogui.press("volumedown")

    elif "remind me" in query:
        import threading
        Speak("What should i remind you for")
        name = getcommand()
        Speak("When Should I Remind You")
        time = getcommand()
        from Feature import Reminder
        tt = time
        tt = tt.replace(".", "")
        tt = tt.upper()
        h = threading.Thread(target=lambda: Reminder(tt, name))

    elif "play" in query:
        import pywhatkit
        query = query.replace("play", "")
        Speak(f"Playing {query}")
        pywhatkit.playonyt(query)

    elif "note" in query:
        Takenote()

    elif "news" in query:
        News()

    elif "alarm" in query:
        Speak(
            "Sir Please Tell Me The Time to set alarm. For Example, Set Alarm to 5:30 A.M")
        tt = getcommand()
        tt = tt.replace("set alarm to ", "")
        tt = tt.replace(".", "")
        tt = tt.upper()
        import threading
        m = threading.Thread(target=lambda: Alarm(tt)).start()

    elif "timer" in query:
        import threading
        query = query.replace("set a timer for ", "")
        query = query.replace("minutes", "")
        query = query.replace("minute", "")
        t = threading.Thread(target=lambda: Timer(int(query))).start()

    else:
        pass
