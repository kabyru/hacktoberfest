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

def checkStats(wealth, fame):
    if (wealth <=0 or fame <= 0 or wealth >= 10 or fame >= 10):
        return False
    return True

lines = []
with open('data/csv/sire.csv', newline='\n') as csvfile:
    csvIn = csv.reader(csvfile, delimiter='\t', quotechar='|')
    for lineInst in csvIn:
        lines.append(lineInst)

wealth = 5
fame = 5
numTurns = 0
speakSpeech("Hello, sire. In this game you will make decisions for the king.  If your wealth or fame drop to zero, then the king will kill you.  If your wealth or fame reach ten, the king will become jealous and have you beheaded. See how many turns you can stay in office.")
while (checkStats(wealth, fame)):
    numTurns += 1
    dw = 0
    df = 0
    lineIndex = math.floor(len(lines) * random.random())
    line = lines[lineIndex]
    speakSpeech(line[8])
    reply = ""
    while reply == "":
        reply = listenSpeech()
    if reply.lower() == "yes":
        speakSpeech(line[9])
        dw = random.randint(int(line[0]),int(line[1])+1)
        df = random.randint(int(line[2]),int(line[3])+1)
    else:
        speakSpeech(line[10])
        dw = random.randint(int(line[4]),int(line[5])+1)
        df = random.randint(int(line[6]),int(line[7])+1)
    wealth += dw
    fame += df
    if dw > 0:
        speakSpeech("Your wealth has increased by " + str(dw) + ". it is now " + str(wealth))
    elif dw < 0:
        speakSpeech("Your wealth has decreased by " + str(abs(dw)) + ". it is now " + str(wealth))
    else:
        speakSpeech("You wealth is " + str(wealth))
    if df > 0:
        speakSpeech("Your fame has increased by " + str(df) + ". it is now " + str(fame))
    elif df < 0:
        speakSpeech("Your fame has decreased by " + str(abs(df)) + ". it is now " + str(fame))
    else:
        speakSpeech("You fame is " + str(fame))
speakSpeech("The king has you beheaded. Congradulations, you stayed in office for " + str(numTurns) + " turns.")
