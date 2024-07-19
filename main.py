import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
recognizer=sr.Recognizer()


#when we dont specify module then we write module name or alias name before class and functions like sr.Recoginizor

#we can import both class and functions,for function which is inside a class we need to import class for them then call the function from its instance

#for functions without class we can do it directly

#sr.Recognizer , Recognizer is a class speech recognition is module as sr alias

#if we would have done like that From speech_recognition import Recognizer then we dont have to do sr.Recognizer instead only Recognizer

recognizer=sr.Recognizer()     #call the class
engine=pyttsx3.init()    #initialised the ttsx engine,its a standalone function otherwise dont know why we did it although its a convention
newsapi="0d8d98318fcc4be5a9fb7bfdff061cf4"
url=" https://newsapi.org/v2/top-headlines?country=us&apiKey=0d8d98318fcc4be5a9fb7bfdff061cf4"
def speak(text):
    engine.say(text)
    engine.runAndWait()
def processCommand(c):
  print("worked")
  if "open google" in c.lower():
    webbrowser.open("https://google.com")
  elif "open facebook" in c.lower():
    webbrowser.open("https://facebook.com")
  elif "open youtube" in c.lower():
    webbrowser.open("https://youtube.com")
  elif c.lower().startswith("play"):
    song=c.lower().split(" ")[1]
    link= musiclibrary.music[song]
    webbrowser.open(link)
  elif "news" in c.lower():
    r=requests.get(url)
    if r.status_code==200:  # 200 HTTP code for request successfula and server returned the data
    #Parse the json without it it wont be identified as dictionary to work with its just a plain text then
     data =r.json()
     articles=data.get('articles',[])   # fetch values in articles key ,if didnt get return []  
     for article in articles:            #?can do for artucles in data,for article in articles
       speak(article['title'])   #function of pyttsx3 to convert text to speech
      #speak title of articles
 
if __name__=="__main__":
 speak("Initialising Jarvis")
 while True:
#Listen for the wake word Jarvis"
#obtain audio from microphone
  r=sr.Recognizer()
  print("Recognizing...")
  try:
    with sr.Microphone() as source:
      print("Listening")
      audio=r.listen(source,timeout=2,phrase_time_limit=1 )
    word=r.recognize_google(audio)
    if (word.lower()=="jarvis"):
      speak("Yes")
      #listen for command
          
      with sr.Microphone() as source:
        print("Jarvis Active...")
        
        audio=r.listen(source)
        command=r.recognize_google(audio)
        print(command)
        processCommand(command)
 
 
 
  except Exception as e: 
    print("Error{0}".format(e))
  '''except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))
  except sr.UnknownValueError:
    print("Could not understand audio")
    speak("I did not understand that. Could you please repeat?")'''