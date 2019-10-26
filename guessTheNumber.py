import speech_recognition as sr     # import the library
import pyttsx3
import csv
import math
import random

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


secretNumber = math.floor(100 * random.random()) + 1

speakSpeech("Guess a Number Between 1 and 100.")
i = 0
while True:
    guess = ""
    while (guess == ""):
        try:
            guess = int(listenSpeech())
        except:
            guess = ""
    if (guess == secretNumber):
        break
    else:
        i += 1
        if (guess < secretNumber):
            speakSpeech(str(guess) + " is too low")
        else:
            speakSpeech(str(guess) + " is too high")
speakSpeech("correct. you guessed in " + str(i) + " tries")

