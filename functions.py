from variables import LINK

import re

# import youtube_dl # client to many multimedia portals
import yt_dlp as youtube_dl

# downloads yt_url to the same directory from which the script runs
def download_audio(yt_url):
    """
    function to download audio from the link
    """

    # Validate the link
    pattern = re.compile(r'^(https?\:\/\/)?(www\.)?(youtube\.com|youtu\.?be)\/.+$')

    # search for a match
    match = pattern.search(yt_url)

    # check if a match was found
    if match:
        print('Valid YouTube link')

        try:
            ydl_opts = {
                'format': 'bestaudio/best',
                'noplaylist' : True,
                'outtmpl': r"C:\Users\Ashish Singh\Downloads\%(title)s.%(ext)s",                
                'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
                }],
            }

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([yt_url])
            
        except:
            print("An error has occurred!!!")
    
    else:
        print("Invalid YouTube link")



from plyer import notification # for sending desktop notification

def send_notification():
    notification.notify(
        title = "YouTube-to-MP3",
        message = "Download complete",
        timeout = 10
    )