import speech_recognition as sr     # import the library
import pyttsx3
from PyDictionary import PyDictionary

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

dictionary=PyDictionary()

speakSpeech("What would you like defined?")
word = listenSpeech()
definition = dictionary.meaning(word)
print(definition)
speakSpeech(definition)

