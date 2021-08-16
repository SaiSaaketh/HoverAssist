import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import webbrowser
import requests
import wikipedia
import sys
import winsound
import webbrowser
import pyautogui
import urllib.request
import re
import winapps
from pyttsx3.drivers import sapi5

# lists
takephoto = {"take a shot", "take a photo", "take a snap",
             "cheese", "Yo take a photo", "take my family photo", "Snap that"}
iamgoing = {"i am going", "I am going out",
            "I'll be right back", "I'm Leaving", "I am leaving"}
hour = int(datetime.datetime.now().hour)


def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def listen():
    listener = sr.Recognizer()
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening.")
                listener.adjust_for_ambient_noise(source)
                listener.dynamic_energy_threshold = 5000
                audio = listener.listen(source, timeout=5.0)
                response = listener.recognize_google(audio, language="en-in")
                print(response)
                if "Hawa" in response or "how" in response:
                    speak("How can I help you?")
                    TaskExec()

                else:
                    pass
        except sr.WaitTimeoutError:
            pass
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            print("Network error.")


def takecommand():
    try:
        listener = sr.Recognizer()
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            listener.dynamic_energy_threshold = 3000
            speak('listening...')
            voice = listener.listen(source, timeout=5.0)
            command = listener.recognize_google(voice, language="en-in")
            print(command)
    except sr.WaitTimeoutError:
        pass
    except sr.UnknownValueError:
        pass
    except sr.RequestError:
        print("Network error.")
    return command.lower()


def wish():
    if hour > 0 and hour < 12:
        speak('Good Morning')
    elif hour > 12 and hour > 15:
        speak('Good Afternoon')
    else:
        speak('Good Evening')


def TaskExec():
    if __name__ == "__main__":
        query = takecommand().lower()
        if query == "open notepad":
            os.system("notepad")
        elif "what is the time" in query:
            min = datetime.datetime.now().minute
            speak(f"It is {hour} hours {min} minutes")
        elif 'browser' in query:
            speak("opening Browser ")
            webbrowser.open("https://www.google.com")
        elif 'open cmd' in query or 'open command prompt' in query:
            speak('Opening CMD')
            os.system("start cmd")
        elif 'camera' in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('Camera', img)
                k = cv2.waitKey(27)
                if k == 27:
                    break
            cap.release()
            cap.destroyAllWindows()
        elif 'ip address' in query:
            ip = requests.get('https://api.ipify.org').text
            speak(f"your ip is {ip}")
        elif 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=3)
            print("According to wikipedia"+results)
            speak('Accoding to wikipedia'+results)
        elif 'open youtube' in query:
            webbrowser.open('www.youtube.com')
        elif 'open stack overflow' in query:
            webbrowser.open('www.stackoverflow.com')
        elif 'search' in query:
            search = query.replace("search", "")
            webbrowser.open(f'www.duckduckgo.com?q={search}')
        elif "whatsapp" in query:
            speak("opening whatsapp")
            whats = "C:\\Users\\JAGADEESWARARAO\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(whats)
        elif 'i am going' in query:
            speak("ok i will security camera to secure your device")
            cam = cv2.VideoCapture(0)
            while cam.isOpened():
                ret, frame1 = cam.read()
                ret, frame2 = cam.read()
                diff = cv2.absdiff(frame1, frame2)
                gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
                blur = cv2.GaussianBlur(gray, (5, 5), 0)
                _, thresh = cv2.threshold(
                    blur, 20, 255, cv2.THRESH_BINARY)
                dilated = cv2.dilate(thresh, None, iterations=3)
                contours, _ = cv2.findContours(
                    dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
                for c in contours:
                    if cv2.contourArea(c) < 20000:
                        continue
                    x, y, w, h = cv2.boundingRect(c)
                    cv2.rectangle(frame1, (x, y),
                                  (x+w, y+h), (0, 255, 0), 2)
                    winsound.PlaySound(
                        'alert.wav', winsound.SND_ASYNC)
                if cv2.waitKey(10) == ord('q'):
                    break
                cv2.imshow('Secure Cam', frame1)
        elif 'bye' in query:
            speak("ok Bye")
            sys.exit()
        elif 'shutdown' in query or 'shut down' in query:
            speak('Shutting Down Windows')
            os.system("shutdown /s /t 00")
        elif 'switch the window' in query:
            speak("I'll switch the window for you")
            pyautogui.hotkey("Alt", "Tab")
        elif 'take a screenshot' in query:
            speak("taking screenshot buddy")
            pyautogui.hotkey("Alt", "prtsc")
        elif "play" in query:
            speak("what should i search yt for")
            search_keyword = takecommand()
            if "" in search_keyword:
                search_keyword = search_keyword.replace(" ", "+")
                html = urllib.request.urlopen(
                    "https://www.youtube.com/results?search_query=" + search_keyword)
                video_ids = re.findall(
                    r"watch\\?v=(\\S{11})", html.read().decode())
                webbrowser.open(
                    "https://www.youtube.com/watch?v=" + video_ids[0])
            else:
                html = urllib.request.urlopen(
                    "https://www.youtube.com/results?search_query=" + search_keyword)
                video_ids = re.findall(
                    r"watch\\?v=(\\S{11})", html.read().decode())
                webbrowser.open(
                    "https://www.youtube.com/watch?v=" + video_ids[0])
        elif "take a note" in query:
            speak("Please tellme what should i take note of")
            hnote = open("hovernotes.txt", "a")
            hnote.write(takecommand())
            hnote.close()
        else:
            speak('i donot know that')


if __name__ == "__main__":
    listen()
