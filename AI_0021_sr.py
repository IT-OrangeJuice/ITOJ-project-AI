import speech_recognition
ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
    print('Robot: Say something, please')
    sound = ear.listen(mic)

try:
    you = ear.recognize_google(sound, language ="vi-VN")
    print('You: ', you)
except:
    you = ''
