import speech_recognition as sr
# Can be installed using "pip install SpeechRecognition" in terminal
from gtts import gTTS
# Can be installed using "pip install gtts" in the terminal
import os

voice = ""
while True:
    e = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = e.listen(source)
            text = e.recognize_google(audio)
            print(text)
            if text == "stop":
                break
            text = e.recognize_google(audio)
            voice = voice + str(text)

        except:
            print("Say Something")
we = gTTS(text=voice, lang='en', slow=False)
we.save("Robo.wav")