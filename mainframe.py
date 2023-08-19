VIEWS = 200 #how many view does it have to have
LANG = "en" #what lagnauge the clips should be
CATEGORY = "League of Legends"
DAYS = 1 #clips from how many days

#from twitch_highlights import TwitchHighlights
import youtube_dl
from twitch_highlights import TwitchHighlights
from twitch_highlights import twitch_api
from datetime import datetime, timedelta
import urllib.request
import io
from PIL import ImageTk, Image
#important api info

twitch_credentials = {
    "client_id" : "get ur client id on twitch",
    "client_secret" : "and put secret and put it here"
}

# #what time to check from to when
# with open("session.txt") as file:
#     started_at = file.read()
# with open("session.txt", "w") as file:
#     file.write(datetime.utcnow())
started_at = datetime.utcnow() - timedelta(days=DAYS) #a day ago
ended_at = datetime.utcnow()

clip_url = "https://api.twitch.tv/helix/clips?id=BitterMushyWaterThisIsSparta--dclNb4qjemNi50t" #example clip

twitch = TwitchHighlights(twitch_credentials=twitch_credentials)
l = twitch_api.login(twitch_credentials)
#this for clip infos

def getclips():
    infoToScrape = ["thumbnail_url", "broadcaster_name", "title", "url"]
    clipinfo = twitch_api.get_clips_by_category(l, CATEGORY, started_at, ended_at)
    info = []
    #this for searching certain elemnts and making it readable
    for video in clipinfo:
        if video["view_count"] < VIEWS or video["language"] != LANG: #skips videos that arent above 100 views and arent english. i tried doing break on if it was and the cataching with for loop, very inefficient lmao
            continue
        videoList = []
        for item, element in video.items():#1st will be what it is "url", "link" and then the element will be what it actually is    
            if item in infoToScrape:
                videoList.append(f"{element}") #videoList.append(f"{item} : {element}")
        info.append(videoList)
    # for i in info:
    #     print(i)
    #     print("\n\n\n")
    return info
    

class WebImage:
    def __init__(self, url):
        with urllib.request.urlopen(url) as u:
            raw_data = u.read()
        #self.image = tk.PhotoImage(data=base64.encodebytes(raw_data))
        image = Image.open(io.BytesIO(raw_data))
        self.image = ImageTk.PhotoImage(image)

    def get(self):
        return self.image
        
def downloadCLIP(twitchLink):
    ydl_opts = {
        'format' : 'bestvideo+bestaudio[ext=mp3]/bestvideo+bestaudio/best',
        'outtmpl': 'video foler\clip.mp4'
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([twitchLink])



# test = twitch.get_top_categories()
# print(test)

# clips = twitch_api.get_category_id(l, category_name="League of Legends")
# print(clips)

