from variables import LINK

import re

import youtube_dl # client to many multimedia portals

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