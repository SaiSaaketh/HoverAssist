import speech_recognition as sr 

listener = sr.Recognizer()
def GetCommand():
    with sr.Microphone() as source:
        listener.pause_threshold = 1
        voice = listener.listen(source)
    try:
        command = listener.recognize_google(voice,language="en-in")
    except Exception as e:
        pass
    return "None" 
command = GetCommand().lower()   
print(command)