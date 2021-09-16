import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say('Hi There I am Alexa')
engine.say('What can I do for you')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            text = listener.recognize_google(voice)
            text = text.lower()
            if 'alexa' in text:
                text = text.replace('alexa', '')
                print(text)


    except:
        pass
    return text

def run_alexa():
    text = take_command()
    print(text)
    if 'play' in text:
        song = text.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in text:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current Time is' +time)

    elif 'who is' in text:
        info = text.replace('who is','')
        details = wikipedia.summary(info, 1)
        print(details)
        talk(details)

    elif 'date' in text:
        talk('I am sorry i am not a human')

    elif 'jokes' in text:
        talk(pyjokes.get_joke())

    else:
        talk('Please say the command again.I did not understand')

while True:
    run_alexa()