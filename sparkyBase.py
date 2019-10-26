import speech_recognition as sr     # import the library
import pyttsx3
import webbrowser
 
r = sr.Recognizer()                 # initialize recognizer
engine = pyttsx3.init()
with sr.Microphone() as source:     # mention source it will be either Microphone or audio files.
    print("Speak Anything :")
    engine.say('Speak Anything.')
    engine.runAndWait()
    audio = r.listen(source)        # listen to the source
    try:
        text = r.recognize_google(audio)    # use recognizer to convert our audio into text part.
        print("You said : {}".format(text))
        engine.say("You said : {}".format(text))
        engine.runAndWait()
    except :
        print("Sorry could not recognize your voice")
        engine.say("Sorry could not recognize your voice")
        engine.runAndWait()