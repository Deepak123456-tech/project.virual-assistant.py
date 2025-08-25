#import required modules
import speech_recognition as sr
import pyttsx3
import os
import datetime
import webbrowser

#create engine
engine =pyttsx3.init()
engine.setProperty("rate",175)

#convert text to speech
def speak(text):
    print("assitant:",text)
    engine.say(text)
    engine.runAndWait()
    return text

#reading commands
def take_command():
 listener=sr.Recognizer()
 with sr.Microphone() as source:
        print("listening ....")
        audio=listener.listen(source)
        try:
            command=listener.recognize_google(audio)
            command=command.lower()
            print("you said :",command)
            return command
        except:
            return ""
        
#run assistant function
def run_assistant():
    command =take_command()
    # if ask what is time 
    if "time" in command:
        time=datetime.datetime.now().strftime("%I,%M,%P")
        speak("the time is {time}")
#if ask open notepad
    elif "open notepad" in command:
        print("opening notepad")
        os.system("notepad")
    elif "open youtube" in command:
        speak("opening youtube ")
        webbrowser.open("https://youtube.com")
    #implementing the search
    elif "hey siri " in command:
        query=command.replace("hey siri","").strip()
        if query:
            url="https://www.google.com/search?q=(query)"
            speak(f"searching for {query}")
            webbrowser.open(url)
        else:
            speak("hey hi,what can i do for you")
    elif "bye" in command or "stop" in command :
        speak("okay bye bye ,see u soon")
        exit()
    else:
        speak(" i can answer questions,open youtube,time or open notepad")

if __name__ == "__main__":
    speak("hi, i am your virtual assitant,today in will assist")
    while True:
       run_assistant()      
    

