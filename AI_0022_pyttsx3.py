import pyttsx3, datetime
mouth = pyttsx3.init()
voice = mouth.getProperty('voices')
mouth.setProperty('voice',voice[1].id) # đặt giọng nói
rate = mouth.getProperty('rate')
mouth.setProperty('rate', rate-70) # Tốc độ nói

def speak(audio):
    print("Robot: "+ audio)
    mouth.say(audio)
    mouth.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%H:%M")
    speak(Time)
speak("Tuấn trần rất toàn năng")
time()