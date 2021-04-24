import pyttsx3#text to speech
import speech_recognition as sr
import datetime#to show date and time
import webbrowser as wb
import os
import smtplib
import requests
#from pprint import pprint
#import json
import psutil
import pyjokes


engine = pyttsx3.init()#initializing pyttsx3
voices = engine.getProperty('voices')#initializing Voices
engine.setProperty('voice',voices[0].id)#mode of voice male, female

def speak(audio):
    engine.say(audio)#says what is in round brackets ()
    engine.runAndWait()#Halts until any return value

def cpu():
    usage=str(psutil.cpu_percent())
    speak("CPU is at"+usage)
    print(usage)
def battery():
    battery = psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)
    print(battery.percent)
def joke():
    joke=pyjokes.get_joke(language='en', category= 'neutral')
    speak(joke)

def wishMe():
    speak("Welcome back sir")#speaks command
    hour = int(datetime.datetime.now().hour)#initialize hour variable which holds hour
    print(hour)
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    Time = datetime.datetime.now().strftime("%I:%M:%S") 
    print(Time)
    print(date)
    print(month)
    print(year)
    speak("the current Time is")
    speak(Time)
    speak("the current Date is")
    speak(date)
    speak(month)
    speak(year)
    if hour>=6 and hour<12:
        speak("Good Morning sir!!!!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!!!!")

    elif hour>=18 and hour<24:
        speak("Good Evening sir!!!!")

    else:
        speak("Good Night sir!!!!!")

    speak("At your Service. Please tell me how can I help You, sir ")
#wishMe()
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        ##r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Sir you Said:{query}\n")
    
    
    except Exception as e:
        print(e)
        print("Say that again Please...")
        speak("Say that again Please...")
        return "0"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Emailaddress', 'Password')
    server.sendmail('Email address', to, content)
    server.close()

def openFile():
    
        speak("what should i open?")
        r = sr.Recognizer()
        with sr.Microphone() as source:
                print('say something!')
                audio = r.listen(source)
                print("done")
        try:
            text = r.recognize_google(audio)
            print(text)
            a="C:/Desktop/"
            os.startfile(a + text)
            b=a+text
            print(b)
        except Exception as e:
            print(e)    
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'search in chrome' in query:
            speak("what should i search?")
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'#Add the Location of the chrome browser

            r = sr.Recognizer()

            with sr.Microphone() as source:
                print('say something!')
                audio = r.listen(source)
                print("done")
            try:
                text = r.recognize_google(audio)
                print('google think you said:\n' +text +'.com')
                wb.get(chrome_path).open(text+'.com')
            except Exception as e:
                print(e)
        
        elif 'how is the weather ai' and 'weather' in query:

           # base URL
            BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
        # City Name
            CITY = "City,Country"
        # API key
            API_KEY = 'Api Key'
        # upadting the URL
            URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
        # HTTP request
            response = requests.get(URL)
        # checking the status code of the request
            if response.status_code == 200:
        # getting data in the json format
                data = response.json()
        # getting the main dict block
                main = data['main']
        # getting temperature
                temperature = main['temp']
                b= temperature - 273.15
        # getting the humidity
                humidity = main['humidity']
        # getting the pressure
                pressure = main['pressure']
        # weather report
                report = data['weather']
                print(f"{CITY:-^30}")
                print(f"Temperature: {b} °C")
                print(f"Humidity: {humidity}")
                print(f"Pressure: {pressure}")
                print(f"Weather Report: {report[0]['description']}")
                engine.say(f"{CITY:-^30}")
                engine.say(f"Temperature: {b}")
                engine.say(f"Humidity: {humidity}")
                engine.say(f"Pressure: {pressure}")
                engine.say(f"Weather Report: {report[0]['description']}")
                engine.runAndWait()
            else:
   # showing the error message
                print("Error in the HTTP request")

 


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        
        elif 'the date' in query:
            year = int(datetime.datetime.now().year)
            month = int(datetime.datetime.now().month)
            date = int(datetime.datetime.now().day)
            speak("the current Date is")
            speak(date)
            speak(month)
            speak(year)


        elif 'email' and 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "receiver email address"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry.I am not able to send this email")     

        elif 'open' in query:
            openFile()

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            joke()
        elif 'battery' in query:
            battery()

        elif 'on light' in query:
            text=''
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            wb.get(chrome_path).open(text+'/ledon')
        elif 'off light' in query:
            text=''
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            wb.get(chrome_path).open(text+'/ledoff')
        elif 'light on' in query:
            text=''
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            wb.get(chrome_path).open(text+'/ledon')
        elif 'light off' in query:
            text=''
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            wb.get(chrome_path).open(text+'/ledoff')     
        elif 'shutdown' in query:
            speak("ok sir shutting down the system")
            quit()
