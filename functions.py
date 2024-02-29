from pytube import YouTube
import os


def downloadVideo(link, verbose=False, directory="videos"):
    yt = YouTube(link)
    file_path = os.path.join(os.path.realpath(__file__), directory)
    yt.streams.get_lowest_resolution().download(file_path)
    if verbose == True:
        print("Downloaded: " + yt.title)
    return yt.title
