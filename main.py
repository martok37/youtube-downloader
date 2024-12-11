import yt_dlp


# Settings

# url adress of youtube video
url = r"https://www.youtube.com/watch?v=4pBo-GL9SRg"

# yt-dlp options
ydl_opts = {
    'format': 'bestaudio/best',  # Pobranie najlepszego strumienia audio
    'postprocessors': [
        { 
            'key': 'FFmpegExtractAudio',

            # WAv
            # 'preferredcodec': 'wav',
            
            # MP3
            'preferredcodec': 'mp3',
            'preferredquality': '192'
        }
    ],
    'outtmpl': 'audio',  # Nazwa pliku wynikowego
}


def main():
    # get info about the video
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url=url, download=False)
        title = info['title']
    
    # Set title as name of output file
    ydl_opts['outtmpl'] = 'output/' + title

    # download audio
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__=="__main__":
    main()