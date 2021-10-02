import pyttsx3  #do pip install pyttsx3 in terminal
import datetime #for wishing and time purpose
import speech_recognition as sr #do pip install speechRecognition
import wikipedia #do pip install wikipedia
import webbrowser #for opening websites
import os #for music function
import smtplib #for email part

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
#voice[1] is for female voice and voice[2] is for male
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening!")  

    speak("Hello sir,I am Friday how may i help you") 
    
def takeCommands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said : {query}\n")
    except Exception as e:
        print(e)
        speak("Please say that again..")
        return "None"        
    return query    
def sendEmail(to,content): #for sending email you should turn off less secure apps in gmail settings
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('s1032190678@gmail.com','Write your password here!')
    server.sendmail('s1032190678@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommands().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            webbrowser.open("youtube.com")
        elif 'google' in query:
            webbrowser.open("google.com")
        elif 'whatsapp web' in query:
            webbrowser.open("web.whatsapp.com")
        elif 'play music' in query:
            music_dlr = 'F:\SONGS'
            songs = os.listdir(music_dlr)      
            print(songs)  
            os.startfile(os.path.join(music_dlr,songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            codePath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'email to ani' in query:
            try:
                speak("What should I say?")
                content = takeCommands()
                to = "singhaniket1501@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")
