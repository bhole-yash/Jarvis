# importing the pyttsx library 
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes

# initialisation 
engine = pyttsx3.init()


# testing 


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    speak("the current time is")
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)


def wishme():
    speak("Welcome back sir!")

    time()

    date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good morning sir!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon sir!")
    elif hour >= 18 and hour < 24:
        speak("Good evening sir!")
    else:
        speak("Good night")
    speak("Whatsup....Is there anyway I can help you!")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing----")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please")

        return "None"
    return query


def jokes():
    speak(pyjokes.get_joke())


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('yashbhole6@gmail.com', 'rcnwnlzvbcpogahd')
    server.sendmail('yashbhole6@gmail.com', to, content)
    server.close()

    # 'sritesh.tcet@gmail.com'


def screenshot():
    img = pyautogui.screenshot()
    img.save("F:\\my-project")


def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at ' + usage)
    battery = psutil.sensors_battery()
    speak("Battery is at ")
    speak(battery.percent)


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if "time" in query:
            time()

        elif 'date' in query:
            date()

        elif 'wikipedia' in query:
            speak("Searching....")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif 'search in chrome' in query:
            speak("what should I search")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            print(search)
            wb.get(chromepath).open_new_tab('www.' + search + '.com')

        elif 'logout' in query:
            os.system("shutdown -l")

        elif 'shutdown' in query:
            os.system("shutdown /s/t l")

        elif 'restart' in query:
            os.system("shutdown /r/t l")
        # elif 'screenshot' in query:
        #     screenshot()
        #     speak("Done!")

        # elif 'play songs' in query:

        elif 'offline' in query:
            quit()


        elif 'play songs' in query:
            songs_dir = 'E:\\downloads2\\VA - 100 Greatest Happy Songs (2020) Mp3 320kbps [PMEDIA] ⭐️'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif 'remember that' in query:
            speak("What should I remember")
            data = takeCommand()
            speak("you said me to remember that" + data)
            remember = open('data.txt', 'w')

            remember.write(data)
            remember.close()

        elif 'cpu' in query:
            cpu()

        elif 'do you remember anything' in query:
            remember = open('data.txt', r)
            speak("you said me to remember that" + remember.read())




        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = 'shreyashbhole193045@gmail.com'
                sendEmail(to, content)
                speak('Email has been sent')
            except Exception as e:
                print(e)
                speak("Unable to send email")

        elif 'joke' in query:
            jokes()

        elif 'offline' in query:
            quit()
