import yt_dlp
import os

def main():
    url = input("Youtube link here: ").strip()

    choice = input("mp3 or mp4 (3/4): ").strip()

    output_path = os.path.dirname(os.path.abspath(__file__))

    if choice == "3":
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": os.path.join(output_path, "%(title)s.%(ext)s"),
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
        }
    elif choice == "4":
        ydl_opts = {
            "format": "bestvideo+bestaudio/best",
            "outtmpl": os.path.join(output_path, "%(title)s.%(ext)s"),
            "merge_output_format": "mp4",
        }
    else:
        print("Invalid choice.")
        return

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    main()