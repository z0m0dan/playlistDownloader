from pytube import Playlist
import sys
from functions import downloadVideo


def playlistDownloader(url, verbose, directory):

    # Create a playlist object
    playlist = Playlist(url)

    # Loop through each video in the playlist and download it
    for video in playlist.videos:
        downloadVideo(video)
