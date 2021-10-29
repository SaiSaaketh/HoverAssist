import datetime
import os  # os module is used to open files and run commands on the cmd and a lot of other features installation:deafult by python
import webbrowser
import cv2
import pyautogui
import pyttsx3  # pyttsx3 is module for text to speech installation:pip install pyttsx3
import requests
# speechrecogntion is the module which is used for recognizing audio and converting into text installation:pip install speechrecogntion
import speech_recognition as sr
from pyttsx3.drivers import sapi5
import functools
from Feature import *

hour = datetime.datetime.now().hour


class HoverAssist:
    
    def __init__(self) -> None:
        self.hour = int(datetime.datetime.now().hour)
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[0].id)

    def speak(self, audio):
        self.engine.say(audio)
        print("                                                ")
        print(f"Hover Said: {audio}")
        self.engine.runAndWait()
        self.engine.stop()
        
    def listen(self):
        while True:
            listener = sr.Recognizer()
            try:
                with sr.Microphone() as source:
                    audio = listener.listen(source, timeout=1.0)
                    response = listener.recognize_google(audio)
                    response = response.lower()
                    if "hawa" in response or "how" in response:
                        self.speak("How can I help you?")
                        self.Analyze()
                    else:
                        pass
            except sr.WaitTimeoutError:
                pass
            except sr.UnknownValueError:
                pass
            except sr.RequestError:
                print("Network error.")

    def takecommand(self):
        listener = sr.Recognizer()
        command = ""
        try:
            with sr.Microphone() as source:
                voice = listener.listen(source, phrase_time_limit=4)
                command = listener.recognize_google(voice)
                print(f"User Said: {command}")
                print("                                      ")
        except sr.WaitTimeoutError:
            pass
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            print("Network error.")
        return command.lower()
    
    @functools.lru_cache()
    def wish(self, hour):
        if hour > 0 and hour < 12:
            self.speak('Good Morning')
        elif hour > 12 and hour > 15:
            self.speak('Good Afternoon')
        else:
            self.speak('Good Evening')

    def Analyze(self):
        query = self.takecommand().lower()
        if query == "open notepad":
            os.system("notepad")

        elif "what is the time" in query:
            min = datetime.datetime.now().strftime("%I:%M %p")
            self.speak(f"It is {min}")

        elif 'browser' in query:
            self.speak("opening Browser ")
            webbrowser.open("https://www.google.com")

        elif 'open cmd' in query or 'open command prompt' in query:
            self.speak('Opening CMD')
            os.system("start cmd")

        elif 'open camera' in query:
            self.capture = cv2.VideoCapture(0)
            while True:
                ret, img = self.capture.read()
                cv2.imshow('Camera', img)
                k = cv2.waitKey(27)
                if k == 27:
                    break

        elif 'close camera' in query:
            self.capture.release()
            self.capture.destroyAllWindows()

        elif 'ip address' in query:
            ip = requests.get('https://api.ipify.org').text
            self.speak(f"your ip is {ip}")

        elif 'wikipedia' in query:
            self.speak('Searching Wikipedia')
            import wikipedia
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=3)
            self.speak('Accoding to wikipedia'+results)

        elif 'open youtube' in query:
            self.speak("Opening Youtube")
            webbrowser.open('www.youtube.com')

        elif 'open stack overflow' in query:
            self.speak("Opening Stackoverflow")
            webbrowser.open('www.stackoverflow.com')

        elif 'search' in query:
            self.speak("Searching The Internet")
            search = query.replace("search", "")
            webbrowser.open(f'www.google.com/search?q={search}')

        elif 'i am going' in query:
            self.speak(
                "ok i will open ..security camera. to secure your device")
            Security_Cam()

        elif 'open' in query.lower():
            query = query.replace("open", "")
            query = query.replace("chrome", "")
            self.speak(f"Opening {query} ")
            Webopener.webopen(query=query)

        elif "weather" in query:
            from Feature import Weather
            w = Weather()
            self.speak(w)
            
        elif 'how' in query:
            import pywikihow
            how = pywikihow.search_wikihow(query, max_results=1)
            assert len(how) == 1
            self.speak(how[0].summary)

        elif 'shutdown' in query or 'shut down' in query:
            self.speak('Shutting Down Windows')
            os.system("shutdown /s /t 00")

        elif 'switch the window' in query:
            self.speak("I'll switch the window for you")
            pyautogui.hotkey("Alt", "Tab")

        elif 'take a screenshot' in query:
            self.speak("taking screenshot buddy")
            pyautogui.hotkey("Win", "prtsc")

        elif "volume up" in query:
            pyautogui.press("volumeup")

        elif "volume down" in query:
            pyautogui.press("volumedown")

        elif "remind me" in query:
            import threading
            self.speak("What should i remind you for")
            name = self.takecommand()
            self.speak("When Should I Remind You")
            time = self.takecommand()
            from Feature import Reminder
            tt = time
            tt = tt.replace(".", "")
            tt = tt.upper()
            h = threading.Thread(target=lambda: Reminder(tt, name))

        elif "play" in query:
            import pywhatkit
            query = query.replace("play", "")
            self.speak(f"Playing {query}")
            pywhatkit.playonyt(query)

        elif "note" in query:
            Takenote()

        elif "alarm" in query:
            self.speak(
                "Sir Please Tell Me The Time to set alarm. For Example, Set Alarm to 5:30 A.M")
            tt = self.takecommand()
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


Hover = HoverAssist()
Hover.wish(hour=hour)
Hover.listen()
