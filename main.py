import tkinter as tk
import customtkinter as ctk
from webbrowser import open_new
from youtube_upload.client import YoutubeUploader
from os import remove
from mainframe import *

def openTab():
    open_new(twitchLink)


def YTupload():
    global twitchLink, thumbnail, clips, videoNum, name
    broadcaster_name = clips[videoNum][name]
    try:
        remove("video foler\clip.mp4")
    except:
        print("Nothing to delete")
    downloadCLIP(twitchLink)
    uploader = YoutubeUploader(secrets_file_path="ur client secerent goes here")
    uploader.authenticate()
    title = vidTitle.get()
    options = {
    "title" : title, # The video title
    "description" : f"Credit: https://www.twitch.tv/{broadcaster_name}\nIf you want me to delete a video contact me!", # The video description
    "tags" : ["Pro Player Clips", "LoL", "League of Legends", "League", "League Clips", broadcaster_name],
    "categoryId" : "20", #20 is gaming, 23	Comedy, 24	Entertainment
    "privacyStatus" : "public", # Video privacy. Can either be "public", "private", or "unlisted"
    "kids" : False, # Specifies if the Video if for kids or not. Defaults to False.
    #"thumbnailLink" : thumbnail # Optional. Specifies video thumbnail.
    }
    uploader.upload("video foler/clip.mp4", options)



def nextvid():
    global videoNum, twitchLink
    #if its the max dont change
    if videoNum == len(clips)-1:
        return
    videoNum +=1
    #rechange the variables
    twitchLink = clips[videoNum][url]
    thumbnail = clips[videoNum][thumbnail_url]
    twitchTitle = clips[videoNum][title]
    broadcaster_name = clips[videoNum][name]
    #configure them and change it to update
    TwitchLabel.configure(text=f"{twitchTitle}\n{broadcaster_name}")
    img = WebImage(thumbnail).get()
    LinkButton.configure(image=img)
    win.update()



def previousvid():
    global videoNum, twitchLink
    #if first page then dont change
    if videoNum == 0:
        return
    videoNum -=1
    #rechange the variables
    twitchLink = clips[videoNum][url]
    thumbnail = clips[videoNum][thumbnail_url]
    twitchTitle = clips[videoNum][title]
    broadcaster_name = clips[videoNum][name]
    #configure them and change it to update
    TwitchLabel.configure(text=f"{twitchTitle}\n{broadcaster_name}")
    img = WebImage(thumbnail).get()
    LinkButton.configure(image=img)
    win.update()
    

#getting a list full of lists with [url, creator name, title, thumbnail_url]
clips = getclips()
videoNum = 0
url = 0
name = 1
title = 2
thumbnail_url = 3
#Settings
ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue")


#varaibles
twitchLink = clips[videoNum][url]
thumbnail = clips[videoNum][thumbnail_url]
twitchTitle = clips[videoNum][title]
broadcaster_name = clips[videoNum][name]
#Frame
win = ctk.CTk()
win.geometry("720x480")
win.title("Twitch League Clips to Youtube")

#Title of Clip
fontLabel = ctk.CTkFont(family="Impact", size=25)
TwitchLabel = ctk.CTkLabel(win, text=f"{twitchTitle}\n{broadcaster_name}", font=fontLabel)
TwitchLabel.pack(pady=5)

#Link, maybe make this the thumbnail, and then on click open the tab

img = WebImage(thumbnail).get()
LinkButton = ctk.CTkButton(win, fg_color="transparent", border_width=3, border_color="gray", text="", image=img,command=openTab)
LinkButton.pack()
# twitchL = "https://www.twitch.tv/loltyler1/clip/BitterMushyWaterThisIsSparta--dclNb4qjemNi50t"
# LinkButton = ctk.CTkButton(win, text=twitchL, command=openTab)
# LinkButton.pack()


#upload Button
fontD = ctk.CTkFont(size=15)
upload = ctk.CTkButton(win, height=40, width=200, text="Upload!", font=fontD, command=YTupload) #command = on click run this function
#download.pack(pady=20)
upload.place(rely=0.92, relx= 0.5, anchor=ctk.CENTER)



#title of video
vid_var = tk.StringVar()
vidTitle = ctk.CTkEntry(win, width=350, height=40, textvariable=vid_var)
vidTitle.place(relx=0.6, rely=0.82, anchor=ctk.CENTER)
titleLabel = ctk.CTkLabel(win, text="Title Of Vid:", font=fontLabel)
titleLabel.place(relx=0.25, rely=0.82, anchor=ctk.CENTER)

#next and previous tab
next = ctk.CTkButton(win,text_color="black",fg_color="white", text="Next",command=nextvid )#command=lambda: nextvid(videoNum)
previous = ctk.CTkButton(win,text_color="black", fg_color="white", text="Previous",command=previousvid )#command=lambda: previousvid(videoNum)
previous.place(relx=0.25, rely=0.92, anchor=ctk.CENTER)
next.place(relx=0.75, rely=0.92, anchor=ctk.CENTER)
#Keep it running
win.mainloop()

    






# anchor − The exact spot of widget other options refer to: may be N, E, S, W, NE, NW, SE, or SW, compass directions indicating the corners and sides of widget; default is NW (the upper left corner of widget)

# bordermode − INSIDE (the default) to indicate that other options refer to the parent's inside (ignoring the parent's border); OUTSIDE otherwise.

# height, width − Height and width in pixels.

# relheight, relwidth − Height and width as a float between 0.0 and 1.0, as a fraction of the height and width of the parent widget.

# relx, rely − Horizontal and vertical offset as a float between 0.0 and 1.0, as a fraction of the height and width of the parent widget.