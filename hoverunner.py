import speech_recognition as sr
import hover
import cv2
from tkinter import *

listener = sr.Recognizer()
def Recognizer():
    with sr.Microphone() as source:
        voice = listener.listen_in_background(source)
        command = listener.recognize_google(voice)
        if 'hover' in command:
            hover.run_hover()
            
while True:
    Recognizer()
