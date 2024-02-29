import argparse
from playlistDownloader import playlistDownloader

parser = argparse.ArgumentParser(description='Playlist downloader, downloads all videos from a youtube playlist',
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter, usage='%(prog)s [-u URL]')
parser.add_argument(
    '-u', '--url', help='The url of the playlist to download', required=True)
parser.add_argument(
    '-v', '--verbose', help='Show all the information of the downloaded videos', action='store_true', required=False)
parser.add_argument('-d', '--directory',
                    help='The directory to download the videos to', default='The name of the playlist', required=False)

args = parser.parse_args()

if __name__ == "__main__":
    playlistDownloader(args.url, args.verbose, args.directory)

