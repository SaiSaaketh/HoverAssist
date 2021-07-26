import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import pywhatkit
import webbrowser
from requests import get
from bs4 import BeautifulSoup
import wikipedia
import sys
import winsound
import smtplib
import speech_recognition as sr
from email.message import EmailMessage
import webbrowser

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
print(voice)
engine.setProperty('voices',voice[2].id)
rate = engine.getProperty('rate')
engine.setProperty('rate',170)
 
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def takecommand():
    try:
        with sr.Microphone() as source:
            speak('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
    except:
        pass
    return command
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12:
        speak('Good Morning')
    elif hour > 12 and hour > 15:
        speak('Good Afternoon')
    else:
         speak('Good Evening')


def TaskExec():
        if __name__ == "__main__":
  
    elif hour>12 and hour >15:
        speak('Good Afternoon')
    else:
         speak('Good Evening')         
def TaskExec():
        if __name__ == "__main__":
                query = takecommand().lower()
                if 'open notepad' in query:
                    speak('Opening Notepad')
                    npath = "C:\\Windows\\system32\\notepad.exe"
                    os.startfile(npath)
                elif 'open cmd' in query or 'open query prompt' in query:
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
<<<<<<< HEAD
                elif 'security camera' in query or 'i am going' in query:
=======
                elif 'security camera' in query or 'i am going out' in query:
>>>>>>> 2eb495b (Initial commit)
                    cam = cv2.VideoCapture(0)
                    while cam.isOpened():
                            ret, frame1 = cam.read()
                            ret, frame2 = cam.read()
                            diff = cv2.absdiff(frame1, frame2)
                            gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
                            blur = cv2.GaussianBlur(gray, (5, 5), 0)
<<<<<<< HEAD
                            _, thresh = cv2.threshold(
                                blur, 20, 255, cv2.THRESH_BINARY)
                            dilated = cv2.dilate(thresh, None, iterations=3)
                            contours, _ = cv2.findContours(
                                dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
=======
                            _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
                            dilated = cv2.dilate(thresh, None, iterations=3)
                            contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
>>>>>>> 2eb495b (Initial commit)
                            # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
                            for c in contours:
                                if cv2.contourArea(c) < 20000:
                                    continue
                                x, y, w, h = cv2.boundingRect(c)
<<<<<<< HEAD
                                cv2.rectangle(frame1, (x, y),
                                              (x+w, y+h), (0, 255, 0), 2)
                                winsound.PlaySound(
                                    'alert.wav', winsound.SND_ASYNC)
                            if cv2.waitKey(10) == ord('q'):
                                break
                            cv2.imshow('Secure Cam', frame1)
                elif 'bye' in query:
                    speak("ok Bye")
=======
                                cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
                                winsound.PlaySound('alert.wav', winsound.SND_ASYNC)
                            if cv2.waitKey(10) == ord('q'):
                                break
                            cv2.imshow('Granny Cam', frame1)
                elif 'i donot need anything' in query:
                    speak("thanks")
>>>>>>> 2eb495b (Initial commit)
                    sys.exit()
                elif 'shutdown' in query or 'shut down' in query:
                    speak('Shutting Down Windows')
                    os.system("shutdown /s /t 00")
                elif 'email' in query:
<<<<<<< HEAD
=======
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
>>>>>>> 2eb495b (Initial commit)
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
<<<<<<< HEAD

                    def get_email_info():
                            speak('To Whom you want to send email')
                            name = takecommand()
                            receiver = email_list[name]
                            print(receiver)
                            speak('What is the subject of your email?')
                            subject = takecommand().lower()
                            speak('Tell me the text in your email')
                            message = takecommand().lower()
                            send_email(receiver, subject, message)
                            speak('Hey SaiSaketh. Your email is sent')
                            speak('Do you want to send more email?')
                            send_more = takecommand().lower()
                            if 'yes' in send_more:
                                get_email_info()
                    get_email_info()
                elif 'shutdown' in query or 'shut down' in query:
                    speak('Shutting Down Windows')
                    os.system("shutdown -s 0")
=======
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
                elif 'on chrome' in query:
                    bravepath = "C://Program Files//BraveSoftware//Application//brave.exe"
                    query= query.replace('on chrome','')
                    if 'dot' in query:
                        query = query.replace('dot','.')         
                        webbrowser.open(query)
                elif 'i donot need anything' in query or 'bye' in query:
                    sys.exit()    
                elif 'shutdown' in query or 'shut down' in query:
                    speak('Shutting Down Windows')
                    os.system("shutdown -s 0")               
>>>>>>> 2eb495b (Initial commit)
                elif 'join my english class' in query:
                    webbrowser.open("https://us04web.zoom.us/j/6683041782?pwd=Ry9oQVJqM0hkTzJSaEtCY2owS21hQT09")
                elif 'join my history class' in query:
                    webbrowser.open("https://us04web.zoom.us/j/2740958675?pwd=bDlUVXFVckg1SWJOR1lQbjJQZUhNUT09")
<<<<<<< HEAD
                elif 'join my class' in query:
                    webbrowser.open("https://us02web.zoom.us/j/6797112315?pwd=YVRudmRWZXBmTnloUlVTSHFqZmpmQT09")
                    pyautogui.press("enter")   
                elif 'whatsapp' in query:
                    speak("opening Whatsapp")
                    whats = "C:\\Users\\JAGADEESWARARAO\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
                    os.startfile(whats)
                elif 'pause' in query:
                   pyautogui.press("space")
                elif 'switch the window' in query:
                    speak("I'll switch the window for you")
                    pyautogui.hotkey("Alt","Tab")
                elif 'take a screenshot' in query:
                    speak("taking screenshot buddy")
                    pyautogui.hotkey("Alt","prtsc")
                elif "play" in query:
                    speak("what should i search yt for")
                    search_keyword = takecommand()
                    if "" in search_keyword:
                        search_keyword = search_keyword.replace(" ","+")
                        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
                        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
                        webbrowser.open("https://www.youtube.com/watch?v=" + video_ids[0])
                    else:
                         html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
                         video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
                         webbrowser.open("https://www.youtube.com/watch?v=" + video_ids[0])
                else:
                    speak('i donot know that')
if __name__ == "__main__":
    while True:
        TaskExec()
=======
                elif 'whatsapp' in query:
                    speak("opening Whatsapp")
                    whats = "C:\\Users\\JAGADEESWARARAO\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
                    os.startfile(whats)     
                else:
                    speak('i donot know that')     
if __name__ == "__main__":
        while True:
            speak('Starting Hover')
            wish()    
            while True:
                command = takecommand()
                if 'hawa' in command or 'hover' in command :
                    TaskExec()
                elif 'shut up' in command or 'goodbye' in command:
                    sys.exit()
                else:
                  hoverbusy = "no" 
>>>>>>> 2eb495b (Initial commit)
