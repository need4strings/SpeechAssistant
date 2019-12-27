import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            cat_speak('Sorry, I did not get that...')
        except sr.RequestError:
            cat_speak('Sorry, my speech service is down')
        return voice_data

def cat_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'what is your name' in voice_data:
        cat_speak('My name is Cat!')
    if 'what time is it' in voice_data:
        cat_speak(ctime())
    if 'search google' in voice_data:
        cat_speak('What do you want to search for?')
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        cat_speak('Here is what I found for ' + search)
    if 'search youtube' in voice_data:
        cat_speak('What video would you like to watch?')
        search = record_audio()
        url = 'https://www.youtube.com/results?search_query=' + search
        webbrowser.get().open(url)
        cat_speak('Here is what I found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        cat_speak('Here is the location of ' + location)
    if 'open Netflix' in voice_data:
        cat_speak('Opening Netflix...')
        url = 'https://www.netflix.com/browse'
        webbrowser.get().open(url)
    if 'what is your purpose' in voice_data:
        cat_speak('I pass the butter!')
    if 'create a random recipe' in voice_data:
        url = 'https://www.randomlists.com/random-recipes'
        webbrowser.get().open(url)
        cat_speak('Here is your recipe for today, looks delicious!')
    if ('I want to play a game') in voice_data:
        url = 'https://findtheinvisiblecow.com'
        webbrowser.get().open(url)
        cat_speak('This one is fun!')
    if ('sleep') in voice_data:
        cat_speak('GoodBye Antonio!')
        exit()
    

time.sleep(1)
cat_speak('Hello, how can I help you today?')
while 1:
    voice_data = record_audio()
    respond(voice_data)