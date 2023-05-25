from youtube_search import YoutubeSearch
import webbrowser
import time

def search_youtube(text):
    while True:
        result = YoutubeSearch("text", max_results=10).to_dict()
        if result:
            break
    url = "https://www.youtube.com/" + result[0]['url_suffix']
    webbrowser.open(url)
    time.sleep(1)
search_youtube("python")
