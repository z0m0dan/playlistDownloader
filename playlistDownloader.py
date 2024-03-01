from pytube import Playlist
from functions import downloadVideo


def playlistDownloader(url, directory):

    # Create a playlist object
    playlist = Playlist(url)

    print(f"Downloading {playlist.title} playlist")
    # Loop through each video in the playlist and download it
    for video in playlist.video_urls:
        downloadVideo(video, directory)


if __name__ == "__main__":
    pass
