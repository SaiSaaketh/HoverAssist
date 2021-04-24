import smtplib
import speech_recognition as sr
from email.message import EmailMessage
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voices',voice[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-13)

def talk(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
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
    talk('To Whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject = get_info()
    talk('Tell me the text in your email')
    message = get_info()
    send_email(receiver, subject, message)
    talk('Hey SaiSaketh. Your email is sent')
    talk('Do you want to send more email?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()


get_email_info()
