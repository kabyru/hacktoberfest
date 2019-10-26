import speech_recognition as sr     # import the library
import pyttsx3
import math
import random
import time
import csv
from googletrans import Translator


r = sr.Recognizer()                 # initialize recognizer
engine = pyttsx3.init()

def listenSpeech():
    with sr.Microphone() as source:     # mention source it will be either Microphone or audio files.
        print("Speak Anything :")
        engine.say('Speak Anything.')
        engine.runAndWait()
        audio = r.listen(source)        # listen to the source
        try:
            text = r.recognize_google(audio)    # use recognizer to convert our audio into text part.
            print("You said : {}".format(text))
        except:
            text = ""
            print("Input Fail")
        return text

def speakSpeech(text):
    with sr.Microphone() as source:     # mention source it will be either Microphone or audio files.
        engine.say("You said : {}".format(text))
        engine.runAndWait()

def translateSpeech():

    with sr.Microphone() as source:
        #Token IDs for installed Microsoft TTS voices
        englishID = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
        germanID = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_DE-DE_HEDDA_11.0"
        spanishID = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0"
        japaneseID = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_JA-JP_HARUKA_11.0"
        russianID = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"
        chineseID = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ZH-CN_HUIHUI_11.0"

        print("What are we translating today?")
        engine.say("What are we translating today?")
        engine.runAndWait()
        audio = r.listen(source)
        try:
            translateText = r.recognize_google(audio)
            print("You said: {}".format(translateText))

            print("Into what language?")
            engine.say("Into what language?")
            engine.runAndWait()
            audio = r.listen(source)

            try:
                languageChoice = r.recognize_google(audio)
                if (languageChoice.lower() == "german"):
                    langDest = 'de'
                    engine.setProperty("voice", germanID)
                    print("Translating to German...")
                elif (languageChoice.lower() == "spanish"):
                    langDest = 'es'
                    engine.setProperty("voice", spanishID)
                    print("Translating to Spanish...")
                elif (languageChoice.lower() == "japanese"):
                    langDest = 'ja'
                    engine.setProperty("voice", japaneseID)
                    print("Translating to Japanese...")
                elif (languageChoice.lower() == "russian"):
                    langDest = "ru"
                    engine.setProperty("voice", russianID)
                    print("Translating to Russian...")
                elif (languageChoice.lower() == "chinese"):
                    langDest = "zh-CN"
                    engine.setProperty("voice", chineseID)
                    print("Translating to Chinese...")
            except:
                print("Sorry, this language is not supported yet.")
                engine.say("Sorry, this language is not supported yet.")
                engine.runAndWait()
                return ""

            translator = Translator()
            translatedText = translator.translate(translateText, dest=langDest)
            print("Translated into " + translatedText.dest + ":")
            print(translatedText.text)
            engine.say(translatedText.text)
            engine.runAndWait()
            engine.setProperty("voice", englishID)
        except:
            translatedText = ""
            print("Input Fail")
        return translatedText

def tellJoke():
    with open('data/csv/joke.csv', newline='\n') as csvfile:
        csvIn = csv.reader(csvfile, delimiter='\t', quotechar='|')
        lines = []
        for lineInst in csvIn:
            lines.append(lineInst)
        print(lines)
        print(len(lines))
        lineIndex = math.floor(len(lines) * random.random())
        line = lines[lineIndex]
        print(line)

    speakSpeech(line[0])
    for i in range(1,len(line)):
        if line[i] == "*":
            listenSpeech()
            continue
    time.sleep(.5)
    speakSpeech(line[i])

            




text = listenSpeech()
speakSpeech(text)
if (text.lower() == "translate"):
    translate = translateSpeech()
