from sys import meta_path
import pyttsx3 as pts
import pyaudio
import speech_recognition as sr


engine = init()
voices = engine.getProperty("voices")
print(voices[0].id)
engine.setProperty("voices", voices[0].id)
volume = engine.getProperty('volume')
engine.setProperty('volume', 10.0)


introduction = ['hey there', 'hello']
speak(introduction)
engine.runAndWait()


def spaek(input):
    engine.say(input)
    engine.runAndWait()
    speak("how are yoy fine what about you")


recog = sr.Recognizer()
with sr.Microphone() as source:
    print("microphone started")
    audio = recog.listen(source)
    try:
        text = recog.recognize_google(audio)
        print(text)
    if text == "hello":
        speak("Wellcome to Love Guru virtual intelligence chatbot.At your service sir.")
    elif text == "hi":
        speak("Wellcome to Love Guru virtual intelligence chatbot.At your service sir.")

    elif text == ("thanks"):
        speak("your welcome", "no problem")
    elif text == ("thank you"):
        speak("your welcome", "no problem")
    elif text == ("Love Guru"):
        speak("Yes sir?", "What can I do for you love?")
    elif text == ("how are you"):
        speak("i am fine love.")
    elif text == ("what is your name"):
        speak("My name is Love Guru ,at your service love")
    elif text == ("I Love You"):
        speak("I Love You To.")
    elif text == ("DO you love me"):
        speak("Yes,I do love you.")
    elif text == ("bye"):
        speak("Bye Love have a good day.", "love chatbot is now offline")
    elif text == ("Good Morning"):
        speak("good morning love.")
    elif text == ("good afternoon"):
        speak("good afternoon love")
    elif text == ("good night"):
        speak("good night love")
    else:
        speak("I am not able to understand you.", "sorry love.")
    except:
        print("please speaak again")


print("THANK YOU FOR USING LOVE CHATBOT", "HAVE A GOOD DAY")

