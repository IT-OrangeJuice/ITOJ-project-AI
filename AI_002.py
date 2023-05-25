import speech_recognition as sr
ear = sr.Recognizer()
with sr.Microphone() as mic:
    audio = ear.listen(mic)



