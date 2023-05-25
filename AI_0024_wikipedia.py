# Thư viện wikipedia
import wikipedia
try:
    wikipedia.set_lang("vi")
    infor = wikipedia.summary("Python là gì")
    print(infor)
except:
    print("Tôi không tìm thấy thứ bạn muốn tìm")