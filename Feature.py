import pyttsx3
import threading
import speech_recognition as sr
import datetime
import os
import cv2
import webbrowser
import requests
import wikipedia
import winsound
import webbrowser
import pyautogui
from pyttsx3.drivers import sapi5
import pywhatkit
import pywikihow
from googlesearch import search
import webbrowser

hour = int(datetime.datetime.now().hour)
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    print("                                                  ")
    print(f"Hover Said: {audio}")
    engine.runAndWait()   
    self.engine.stop()


def takecommand():
    try:
        listener = sr.Recognizer()
        with sr.Microphone() as source:
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print(command)
    except sr.WaitTimeoutError:
        pass
    except sr.UnknownValueError:
        pass
    except sr.RequestError:
        print("Network error.")
    return command.lower()


def Security_Cam():
    speak("ok i will open ..security camera. to secure your device")
    cam = cv2.VideoCapture(0)
    while cam.isOpened():
        ret, frame1 = cam.read()
        ret, frame2 = cam.read()
        diff = cv2.absdiff(frame1, frame2)
        gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=3)
        contours, _ = cv2.findContours(
            dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for c in contours:
            if cv2.contourArea(c) < 20000:
                continue
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
            winsound.PlaySound('alert.wav', winsound.SND_ASYNC)
        if cv2.waitKey(10) == ord('q'):
            break
        cv2.imshow('Secure Cam', frame1)


def Webopener():
    USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"

    def webopen(query):
        # scraping data
        urls = []
        for j in search(query=query, tld="co.in", num=1, stop=1, pause=1):
            webbrowser.open(j)
    print("done")


def Alarm(Timing):
    try:
        altime = str(datetime.datetime.now().strptime(Timing, "%I:%M %p"))
    except ValueError:
        speak("I think I didn't catch it in a bit please say that again")
        Timimg = takecommand()
        altime = str(datetime.datetime.now().strptime(Timing, "%I:%M %p"))
    altime =  altime[11:-3]

    Horeal = altime[:2]
    Horeal = int(Horeal)
    Mireal = altime[3:5]
    Mireal = int(Mireal)
    speak(f"Done Set an Alarm for {Timing}")

    while True:
        if Horeal == datetime.datetime.now().hour:
            if Mireal == datetime.datetime.now().minute:
                speak("The alarm has been completed")
                winsound.PlaySound('alert.wav', winsound.SND_FILENAME)

        elif Mireal<datetime.datetime.now().minute:
            break


def Weather():
    from bs4 import BeautifulSoup
    import requests
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    res = requests.get(f'https://www.google.com/search?q=weather&oq=weather&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',headers=headers)
    soup = BeautifulSoup(res.text,'html.parser')   
    location = soup.select('#wob_loc')[0].getText().strip()         
    info = soup.select('#wob_dc')[0].getText().strip() 
    weather = soup.select('#wob_tm')[0].getText().strip()
    precipitation = soup.select('#wob_pp')[0].getText().strip()
    humidity = soup.select('#wob_hm')[0].getText().strip()
    windspeed =soup.select('#wob_ws')[0].getText().strip()
    information = f"It is {weather}°F There are {precipitation} % chances of rainfall It is {info}.the wind is blowing in a speed of {windspeed}. The humidity is {humidity} % in {location} "
    return information


def Takenote():
            speak("What is The Name of the Note")
            name = takecommand()
            speak("Please Tell Me What Should I Take Note Of")
            hnote = open(name, "a")
            note = takecommand()
            hnote.write(f"{note}\n")
            hnote.close()


def Reminder(Timing,reminder):
    import datetime
    import winsound

    altime = str(datetime.datetime.now().strptime(Timing, "%I:%M %p"))

    altime =  altime[11:-3]

    Horeal = altime[:2]
    Horeal = int(Horeal)
    Mireal = altime[3:5]
    Mireal = int(Mireal)
    speak(f"Done Set an Reminder for {Timing} and {reminder}")

    while True:
        if Horeal == datetime.datetime.now().hour:
            if Mireal == datetime.datetime.now().minute:
                print(reminder)
                winsound.PlaySound('alert.wav', winsound.SND_FILENAME)

        elif Mireal<datetime.datetime.now().minute:
            break


def Timer(mins):
    import time

    secs = mins*60
    time.sleep(secs)
    mins = f"{mins}minutes"
    speak(f"The {mins} Timer has been completed")
    winsound.PlaySound('alert.wav', winsound.SND_FILENAME)
    
