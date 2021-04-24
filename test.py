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
import winsound
import smtplib
import speech_recognition as sr
from email.message import EmailMessage
import webbrowser

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
                    break
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
        elif 'security camera' in query or 'i am going out' in query:
             cam = cv2.VideoCapture(0)
             while cam.isOpened():
                    ret, frame1 = cam.read()
                    ret, frame2 = cam.read()
                    diff = cv2.absdiff(frame1, frame2)
                    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
                    blur = cv2.GaussianBlur(gray, (5, 5), 0)
                    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
                    dilated = cv2.dilate(thresh, None, iterations=3)
                    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                    # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
                    for c in contours:
                        if cv2.contourArea(c) < 20000:
                            continue
                        x, y, w, h = cv2.boundingRect(c)
                        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
                        winsound.PlaySound('alert.wav', winsound.SND_ASYNC)
                    if cv2.waitKey(10) == ord('q'):
                        break
                    cv2.imshow('Granny Cam', frame1)
        elif 'i donot need anything' in query:
            speak("thanks")
            sys.exit()
        elif 'shutdown' in query or 'shut down' in query:
             speak('Shutting Down Windows')
             os.system("shutdown /s /t 00")
        elif 'email' in query:
            listener = sr.Recognizer()
            def get_info():
                try:
                    with sr.Microphone() as source:
                        print('listening...')
                        listener.pause_threshold  = 1
                        voice = listener.listen(source)
                        info = listener.recognize_google(voice)
                        print(info)
                        return info.lower()
                except:
                    pass
            def send_email(receiver, subject, message):
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                # Make sure to give app access in your Google account
                server.login('saisaaketh11@gmail.com', 'hover@711')
                email = EmailMessage()
                email['From'] = 'saisaaketh11@gmail.com'
                email['To'] = receiver
                email['Subject'] = subject
                email.set_content(message)
                server.send_message(email)
            email_list = {
                'SaiSaaketh': 'saisaaketh11@gmail.com',
                'Karthik': 'srikarakarthik@gmail.com',
                'akka': 'prabandha.2005@gmail.com',
                'myself': 'saisaaketh52@gmail.com',
            }
            def get_email_info():
                    speak('To Whom you want to send email')
                    name = get_info()
                    receiver = email_list[name]
                    print(receiver)
                    speak('What is the subject of your email?')
                    subject = get_info()
                    speak('Tell me the text in your email')
                    message = get_info()
                    send_email(receiver, subject, message)
                    speak('Hey SaiSaketh. Your email is sent')
                    speak('Do you want to send more email?')
                    send_more = get_info()
                    if 'yes' in send_more:
                        get_email_info()
        elif 'join my english class' in query:
            webbrowser.open("https://us04web.zoom.us/j/6683041782?pwd=Ry9oQVJqM0hkTzJSaEtCY2owS21hQT09")
        elif 'join my history class' in query:
            webbrowser.open("https://us04web.zoom.us/j/2740958675?pwd=bDlUVXFVckg1SWJOR1lQbjJQZUhNUT09")        
        else:
            speak('i donot know that')     