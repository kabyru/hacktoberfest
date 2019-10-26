import speech_recognition as sr     # import the library
import pyttsx3
import csv
import math
import random
import time

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


with open('data/csv/joke.csv', newline='\n') as csvfile:
    csvIn = csv.reader(csvfile, delimiter='\t', quotechar='|')
    lines = []
    for lineInst in csvIn:
        lines.append(lineInst)
    lineIndex = math.floor(len(lines) * random.random())
    line = lines[lineIndex]

speakSpeech(line[0])
for i in range(1,len(line)):
    if line[i] == "*":
        listenSpeech()
        continue
    time.sleep(.5)
    speakSpeech(line[i])
