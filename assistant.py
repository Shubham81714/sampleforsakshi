import pyttsx3
import datetime
import  speech_recognition as sr
import wikipedia
import webbrowser
import os
import requests
from bs4 import BeautifulSoup
import googlesearch
import urllib
# import smtplib



engine =  pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

hour = int(datetime.datetime.now().hour)

def wishme():
    if hour>=0 and hour<12:
        speak('Good Morning!')

    elif hour>=12 and hour<18:
        speak("good afternoon!")

    else:
        speak("good evening!")

if __name__ == "__main__":
    wishme()


speak("sir, I am your virtual assistant. How may I help  you")
# speak("just try some commands such as wikipedia someting or you can just say what can you Do?")

def takecommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('listening.....')

        r.pause_threshold = 1
        
        audio = r.listen(source)


    try:
        print('rechognising')
        query = r.recognize_google(audio, language='en.in')
        print(f"user said : {query}\n")

    except Exception as e:
        print(e)
        print('say it again I didnot get it')
        return "none"

    return query

# def SendEmail(to, content):

if __name__ == "__main__":

    
    if 1:
        query = takecommand().lower()
        '''    ...........logic building.............   '''   

        if 'wikipedia' in query:
            speak('searching wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak('opening youtube ')
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            speak('opening google ')
            webbrowser.open('google.co.in')

        elif 'open facebook' in query:
            speak('open facebook ')
            webbrowser.open('facebook.com')

        elif 'play music' in query:
            speak('ok sure ')
            music_dir = 'E:\\Media\\music\\music for python asistant'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[2]))

        elif  'time' in query:

            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strtime}")

        elif 'open code' in query:
            speak('opening visual studio code ')
            codepath = "C:\\Users\\shubh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'send email' in query:
            speak(" I  am  sorry    sir  Currently  I  cant  sent   emails  but   I  am  working on it.")

        elif 'what can you do' in query:
            speak('since i am in learning you can try that what the time is or wikipedia someting and you can also tell me to open google ')

        elif 'open youtube and play some music' in query:
            speak('opening youtube ')
            webbrowser.open('https://www.youtube.com/watch?v=jJTQhFv6Vk0&list=RDjJTQhFv6Vk0&start_radio=1')

        elif 'who are you' in query:
            speak('I am a virtual assistant that i currently in learning stage')

        elif 'can you speak in hindi'  in query:
            speak('I am sorry but i am learning on some other languages  such as hindi and other ')

    

        else:
            speak('sorry about that but I am learning on it') 
