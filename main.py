# read from console
import typer
from typing_extensions import Annotated
from typing import Optional
from functions import downloadVideo, isPlaylist, downloadPlaylist, isRequirementsFullfilled


def main(url: Annotated[str, typer.Argument()], output: Annotated[Optional[str], typer.Argument()] = "videos", installDeps: Annotated[Optional[str], typer.Option("--install-deps")] = None):
    if isRequirementsFullfilled() == False:
        return
    if (installDeps):
        print("Installing ffmpeg")
        return
    if isPlaylist(url):
        downloadPlaylist(url, output)
    else:
        downloadVideo(url, output)


if __name__ == "__main__":
    typer.run(main)
