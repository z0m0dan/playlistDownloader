## Playlist Downloader

Simple CLI application to download playlists from YouTube and convert them to mp3 files.

### Prerequisites

- [Python 3.8](https://www.python.org/downloads/release/python-380/)
- [pip](https://pip.pypa.io/en/stable/installing/)
- [ffmpeg](https://www.ffmpeg.org/download.html)

### Pre Installation

```bash
pip install -r requirements.txt

# You can run the following command to install ffmpeg
python installdeps.py

# Or you can install it manually
# https://www.ffmpeg.org/download.html 
```

### Usage

```bash
python main.py <playlist_url> <output_dir>
```
