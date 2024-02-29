from pytube import YouTube
from pytube.exceptions import VideoUnavailable
import os
import subprocess

def downloadVideo(video,  directory="videos"):
    try: 
        file_path = os.path.join(os.getcwd(), directory)
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        print("Downloading: " + video)
        yt = YouTube(video, on_complete_callback=onDownloadComplete)
    except VideoUnavailable:
        print("Error downloading: " + video)
        return
    else:
        yt.streams.filter(only_audio=True).first().download(output_path=file_path)
    return video.title


def onDownloadComplete (_, filePath): 
    print("Download complete" + filePath)
    subprocess.run(["ffmpeg", "-i", filePath, filePath.replace(".mp4", ".mp3")])
    
