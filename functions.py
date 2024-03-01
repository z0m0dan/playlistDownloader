from pytube import YouTube, Playlist
from pytube.exceptions import VideoUnavailable
import os
import subprocess


def downloadPlaylist(url, directory="videos"):
    playlist = Playlist(url)
    print(f"Downloading {playlist.title} playlist")
    for video in playlist.video_urls:
        downloadVideo(video, directory)


def isPlaylist(url) -> bool:
    return "playlist" or "list" in url


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
        yt.streams.filter(only_audio=True).first().download(
            output_path=file_path)
    return video.title


def onDownloadComplete(_, filePath):
    print("Download complete" + filePath)

    converter = subprocess.Popen(["ffmpeg", "-i", filePath,
                                  filePath.replace(".mp4", ".mp3")])
    converter.wait()
    os.remove(filePath)


def checkRequirements():
    # Check if ffmpeg is installed
    try:
        subprocess.run(["ffmpeg", "-version"], capture_output=True)
    except FileNotFoundError:
        print("FFmpeg is not installed. Please install it to convert videos to mp3, to install it run main.py --install-deps")
        return False


def isRequirementsFullfilled():
    # Check if ffmpeg is installed
    try:
        subprocess.run(["ffmpeg", "-version"], capture_output=True)
    except FileNotFoundError:
        print("FFmpeg is not installed. Please install it to convert videos to mp3")
        return False
    return True


if __name__ == "__main__":
    pass
