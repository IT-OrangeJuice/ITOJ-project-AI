import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import wikipedia

current = datetime.datetime.now().strftime("%H:%M")
mouth = pyttsx3.init()
voice = mouth.getProperty("voices")
mouth.setProperty("voice", voice[1].id)
rate = mouth.getProperty("rate")
mouth.setProperty("rate", rate-70)
def speak():
    print("Robot: "+ brain)
    mouth.say(brain)
    mouth.runAndWait()
ear = sr.Recognizer()
running = True
brain = "Xin chào, Tôi có thể giúp gì cho bạn"
speak()
while running:
    with sr.Microphone() as mic:
        print("Robot: (  Tôi đang nghe.....  )")
        sound = ear.listen(mic, phrase_time_limit=3)
    try:
        you = ear.recognize_google(sound, language='vi-VN').lower()
        print("Bạn: "+you)
    except:
        you = ""
    def find_info(text):
        try:
            wikipedia.set_lang('vi')
            info = wikipedia.summary(text)
            print(info)
        except:
            info = ''
            brain ="Tôi không tìm được thứ bạn muốn"
            speak(brain)
    if "tìm kiếm" in you or "thông tin" in you:
        find_info(you)
        brain = "đã tìm thấy thông tin cần"
        speak()
    if "tên" in you:
        brain = "Tôi tên là Nước Cam AI TI 01 hoặc bạn có thể gọi tôi là nước cam"
        speak()
    elif "tạo ra" in you or "chế tạo" in you and "bạn" in you:
        brain = "người tạo ra tôi là tuấn trần"
        speak()
    elif "hôm nay" in you and "ăn gì" in you:
        brain = "hôm nay bạn đã ăn vịt quay"
        speak()
    elif "tạm biệt" in you or "biệt" in you or "bye" in you:
        brain = "tạm biệt bạn"
        speak()
        running = False
    elif "giờ" in you or "bây giờ" and "giờ" in you:
        brain = current
        print("bây giờ là: " + current)
        mouth.say("Bây giờ là: " + current)
        mouth.runAndWait()
        running = False
    elif "mở" in you or "bật" in you:
        if "youtube" in you:
            webbrowser.open("https://www.youtube.com/")
            brain = "youtube đã được mở"
            speak()
        if "zalo" in you:
            webbrowser.open("https://chat.zalo.me/")
            brain = "Zalo đã được mở"
            speak()
        if "powerpoint" in you:
            os.startfile("C:/Users/Admin/OneDrive/Máy tính/PowerPoint")
            brain = "powerpoint đã được mở"
            speak()
        if "word" in you:
            os.startfile("C:/Users/Admin/OneDrive/Máy tính/Word")
            brain = "word đã được mở"
            speak()
        if "excel" in you:
            os.startfile("C:/Users/Admin/OneDrive/Máy tính/Excel")
            brain = "excel đã được mở"
            speak()
        if "studio code" in you:
            os.startfile("C:/Users/Admin/OneDrive/Máy tính/Visual Studio Code")
            brain = "Visual Studio code đã được mở"
            speak()
    else:
        print("Robot: tôi không hiểu")
        running = False
        