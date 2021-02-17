import pyttsx3
import speech_recognition as sr
import webbrowser
import socket
import wikipedia
import random
engine =pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('rate', 150)
def speak (audio):
    engine.say(audio)                               
    engine.runAndWait()

hellos=['hello','hi','hey','hai']
helloq=['hey sir','hi','hello sir']
byes=['bye','goodbye','byebye']
byesq=['good bye sir','good luck sir','bye sir']

def commands():
    while 1:
        start=input('Please enter(ENTER)key:')
        amd=sr.Recognizer()
        with sr.Microphone() as source :
            audio=amd.listen(source,phrase_time_limit=5)
        print("stop")

        try:
            text=amd.recognize_google(audio,language='en-US')
            print(text)
        except:
            print('try again!')
            return 0
        if text in hellos:
            speak(random.choice(helloq))
        elif 'open' in text[:4]:
            sitename=text[5:] + '.com'
            webbrowser.open(sitename)
        elif 'what is my IP' in text:
            yourip=socket.gethostbyname(socket.gethostname())
            print(yourip)
            speak(yourip)
        elif 'Wikipedia summary' in text[-17:]:
            speak('please wait this process takes some time')
            wikisum=wikipedia.summary(text[0:-18])
            print(wikisum)
            speak(wikisum)
        elif 'how are you' in text:
            speak('i am fine')
        elif text in byes:
            speak(random.choice(byesq))
            exit()

        
commands()