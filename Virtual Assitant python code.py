import subprocess
import wolframalpha 
import pyttsx3 
import tkinter 
import json 
import random 
import operator 
import speech_recognition as sr 
import datetime 
import wikipedia 
import webbrowser 
import os 
import winshell
import pyjokes 
import feedparser 
import smtplib 
import ctypes 
import datetime 
import requests 
import shutil 
from twilio.rest import Client 
from clint.textui import progress
from bs4 import BeautifulSoup 
import win32com.client as wincl 
from urllib.request import urlopen 


engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id) 
engine.setProperty('rate', 140)
app_id='TAL33P-UPYAK2TP2P'
client = wolframalpha.Client(app_id) 
def speak(audio): 
	engine.say(audio) 
	engine.runAndWait() 

def wishMe(): 
	hour = int(datetime.datetime.now().hour) 
	if hour>= 0 and hour<12: 
		speak("Good Morning Sir !") 

	elif hour>= 12 and hour<18: 
		speak("Good Afternoon Sir !") 

	else: 
		speak("Good Evening Sir !") 

	 
	speak("I am your Assistant,Ms.Jessica") 
	
	

def usrname(): 
	speak("What should i call you sir") 
	uname = takeCommand() 
	speak("Welcome Mister") 
	speak(uname) 
	columns = shutil.get_terminal_size().columns 
	
	print("#####################".center(columns)) 
	print("Welcome Mr.", uname.center(columns)) 
	print("#####################".center(columns)) 
	
	speak("How can i Help you, Sir") 

def takeCommand(): 
	
	r = sr.Recognizer() 
	
	with sr.Microphone() as source: 
		
		print("Listening...") 
		r.pause_threshold = 1
		audio = r.listen(source) 

	try: 
		print("Recognizing...")	 
		query = r.recognize_google(audio, language ='en-in') 
		print(f"User said: {query}\n") 

	except Exception as e: 
		print(e)	 
		print("Unable to Recognizing your voice.") 
		return "Hello"
	
	return query 


if __name__ == '__main__': 
    clear = lambda: os.system('cls') 
    
# This Function will clean any 
# command before execution of this python file 
clear() 
wishMe() 
usrname() 
assname="jessica"
while True: 

    query = takeCommand().lower() 

    # All the commands said by user will be 
    # stored here in 'query' and will be 
    # converted to lower case for easily 
    # recognition of command 
    if 'wikipedia' in query: 
        speak('Searching Wikipedia...') 
        query = query.replace("wikipedia", "") 
        results = wikipedia.summary(query, sentences = 3) 
        speak("According to Wikipedia") 
        print(results) 
        speak(results) 

    elif 'open youtube' in query: 
        speak("Here you go to Youtube\n") 
        webbrowser.open("youtube.com") 

    elif 'open google' in query: 
        speak("Here you go to Google\n") 
        webbrowser.open("google.com")

    elif 'play game' in query:
          speak("lets play guessing game")
          print("lets play guessing game")
          
          speak("rules is simple i will choose any one number from 1 to 10.You will have to guess right number")
          print("rules is simple i will choose any one number from 1 to 10.You will have to guess right number")
          randomnumber=random.randint(1,10)
          inpt12=takeCommand()
          if inpt12==randomnumber and inpt12>=1 and inpt12<=10:
                  speak("congrats u are correct...well played")
                  print("congrats u are correct...well played")
          else:
                  speak("failed..try once more")
                  print("failed..try once more")
    elif 'open gmail' in query:
        speak('okay')
        webbrowser.open('www.gmail.com')

    elif 'open facebook' in query:
        speak('okay')
        webbrowser.open('www.facebook.com')

    elif 'open stackoverflow' in query: 
        speak("Here you go to Stack Over flow.Happy coding") 
        webbrowser.open("stackoverflow.com") 


    elif 'time' in query: 
        strTime = datetime.datetime.now()	 
        speak(strTime)
        print(strTime)

    elif "what\'s up" in query or 'how are you' in query:
        stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
        speak(random.choice(stMsgs))

    elif 'I am fine!' in query or "good" in query: 
        speak("It's good to know that your fine") 

    elif "change my name to" in query: 
        query = query.replace("change my name to", "") 
        assname = query 

    elif "change name" in query: 
        speak("What would you like to call me, Sir ") 
        assname = takeCommand() 
        speak("Thanks for naming me") 

    elif "what's your name" in query or "what is your name" in query: 
        speak("My friends call me") 
        speak(assname)
        print("My friends call me", assname) 

    elif 'exit' in query: 
        speak("Thanks for giving me your time") 
        exit() 

    elif "who made you" in query or "who created you" in query: 
        speak("I have been created by Jay and his teams.") 

    elif 'joke' in query: 
        speak(pyjokes.get_joke()) 

    elif 'search' in query or 'play' in query: 

        query = query.replace("search", "") 
        query = query.replace("play", "")		 
        webbrowser.open(query) 

    elif "who i am" in query: 
        speak("If you talk then definately your human.") 

    elif "why you came to world" in query: 
        speak("Thanks to Hello World. further It's a secret") 

    elif 'power point presentation' in query: 
        speak("opening Power Point presentation") 
        power = r"C:\Users\PandyaJay\Desktop\PPTs\SGP.pptx"
        os.startfile(power) 

    elif 'What is love' in query: 
        speak("It is 7th sense that destroy all other senses") 

    elif "who are you" in query: 
        speak("I am your virtual assistant created by Jay Pandya") 

    elif 'reason for you' in query: 
        speak("I was created as a Minor project by My master ") 

    elif 'change background' in query: 
        ctypes.windll.user32.SystemParametersInfoW(20, 
                                                0, 
                                                "Location of wallpaper", 
                                                0) 
        speak("Background changed succesfully") 

    elif 'news' in query: 

        try: 
           main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=4dbc17e007ab436fb66416009dfb59a8"
           open_bbc_page = requests.get(main_url).json() 
           article = open_bbc_page["articles"] 
           results = [] 
           for ar in article: 
             results.append(ar["title"]) 
          
           for i in range(len(10)): 
              print(i + 1, results[i])
              speak(results[i])
                       
        except Exception as e: 

            print(str(e)) 


    elif 'lock window' in query: 
            speak("locking the device") 
            ctypes.windll.user32.LockWorkStation() 

    elif 'shutdown system' in query: 
            speak("Hold On a Sec ! Your system is on its way to shut down") 
            subprocess.call('shutdown / p /f') 

    elif 'empty recycle bin' in query: 
        winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True) 
        speak("Recycle Bin Recycled") 

    elif "don't listen" in query or "stop listening" in query: 
        speak("for how much time you want to stop me from listening commands") 
        a = int(takeCommand()) 
        time.sleep(a) 
        print(a) 

    elif "where is" in query: 
        query = query.replace("where is", "") 
        location = query 
        speak("User asked to Locate") 
        speak(location) 
        webbrowser.open("https://www.google.com / maps / place/" + location + "") 

    elif "camera" in query or "take a photo" in query: 
        ec.capture(0, " Camera ", "img.jpg") 

    elif "restart" in query: 
        subprocess.call(["shutdown", "/r"]) 

    elif "hibernate" in query or "sleep" in query: 
        speak("Hibernating") 
        subprocess.call("shutdown / h") 

    elif "log off" in query or "sign out" in query: 
        speak("Make sure all the application are closed before sign-out") 
        time.sleep(5) 
        subprocess.call(["shutdown", "/l"]) 

    elif "write a note" in query: 
        speak("What should i write, sir") 
        note = takeCommand() 
        file = open('jessica.txt', 'w') 
        speak("Sir, Should i include date and time") 
        snfm = takeCommand() 
        if 'yes' in snfm or 'sure' in snfm: 
            strTime = datetime.datetime.now()
            file.write(strTime) 
            file.write(" :- ") 
            file.write(note) 
        else: 
            file.write(note) 

    elif "show note" in query: 
        speak("Showing Notes") 
        file = open("jessica.txt", "r") 
        print(file.read()) 
        speak(file.read(6)) 

 
    elif "jessica" in query: 

        wishMe() 
        speak("Jessica in your service Mister") 
        speak(assname) 

    elif "weather" in query: 

        # Google Open weather website 
        # to get API of Open weather 
        api_key = "Api key"
        base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
        speak(" City name ") 
        print("City name : ") 
        city_name = takeCommand() 
        complete_url = base_url + "appid =" + api_key + "&q =" + city_name 
        response = requests.get(complete_url) 
        x = response.json() 

        if x["cod"] != "404": 
            y = x["main"] 
            current_temperature = y["temp"] 
            current_pressure = y["pressure"] 
            current_humidiy = y["humidity"] 
            z = x["weather"] 
            weather_description = z[0]["description"] 
            print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description)) 

        else: 
            speak(" City Not Found ") 
 

    elif "Good Morning" in query: 
        speak("A warm" +query) 
        speak("How are you Mister") 
        speak(assname) 

    # most asked question from google Assistant 
    elif "how are you" in query: 
        speak("I'm fine, glad you me that") 

    else: 
         try:
           res = client.query(query)
           answer = next(res.results).text
           speak(answer)
           print(answer)
         except StopIteration:
           print ("No results")
           continue
        
       
    # elif "" in query: 
        # Command go here 
        # For adding more commands 
