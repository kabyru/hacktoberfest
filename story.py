import speech_recognition as sr     # import the library
import pyttsx3
import random
from os import listdir
from os.path import isfile, join
import math

r = sr.Recognizer()                 # initialize recognizer
engine = pyttsx3.init()

def listenSpeech():
    with sr.Microphone() as source:     # mention source it will be either Microphone or audio files.
        audio = r.listen(source)        # listen to the source
        try:
            text = r.recognize_google(audio)    # use recognizer to convert our audio into text part.
        except:
            text = ""
        return text

def speakSpeech(text):
    with sr.Microphone() as source:     # mention source it will be either Microphone or audio files.
        engine.say("{}".format(text))
        engine.runAndWait()

storyPath = r"data\story"
files = [f for f in listdir(storyPath) if isfile(join(storyPath, f))]
fIndex = math.floor(len(files) * random.random())
f = open(storyPath + "\\" + files[fIndex], "r")
text = f.read()

f.close()
speakSpeech(text)