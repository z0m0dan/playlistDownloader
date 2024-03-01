

def checkOS():
    import platform
    os = platform.system()
    if os == "Windows":
        return "windows"
    elif os == "Linux":
        return "linux"
    elif os == "Darwin":
        return "mac"
    else:
        return "unknown"


def installDeps():
    os = checkOS()
    if os == "mac":
        print("Installing ffmpeg on mac")
        import subprocess
        if subprocess.run(["brew", "-v"]).returncode != 0:
            print("Homebrew is not installed, please install it to install ffmpeg")
            return
        subprocess.run(["brew", "install", "ffmpeg"])
    elif os == "linux":
        print("Installing ffmpeg on linux")
        import subprocess
        subprocess.run(["sudo", "apt", "install", "ffmpeg"])
    elif os == "windows":
        print("Installing ffmpeg on windows")
        import subprocess
        if subprocess.run(["winget", "-v"]).returncode != 0:
            print("Winget is not installed, please install it to install ffmpeg")
            return
        subprocess.run(["winget", "install", "--id=Gyan.FFmpeg", "-e"])


if __name__ == "__main__":
    installDeps()
