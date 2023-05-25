import webbrowser

def search_google(text):
    url = 'https://www.google.com/search?q=' + text
    webbrowser.open(url)

search_google("python code")