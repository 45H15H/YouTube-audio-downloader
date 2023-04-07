#! python3

def run():
    """
    Main function
    """

    print("Youtube audio downloader".center(50, "_"))

    from variables import LINK
    LINK = LINK()
    
    from functions import download_audio
    download_audio(yt_url = LINK)

    from functions import send_notification
    send_notification()

if __name__ == '__main__':
    run()