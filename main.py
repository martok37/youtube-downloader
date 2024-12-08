import yt_dlp

url = r"https://www.youtube.com/watch?v=0hpgMPkfsec"  # Link do wideo na YouTube

# Opcje dla yt-dlp
ydl_opts = {
    'format': 'bestaudio/best',  # Pobranie najlepszego strumienia audio
    'postprocessors': [
        { 
            'key': 'FFmpegExtractAudio',

            # WAv
            # 'preferredcodec': 'wav',
            
            # MP3
            'preferredodec': 'mp3',
            'preferredquality': '192'
        }
    ],
    'outtmpl': 'audio',  # Nazwa pliku wynikowego
}

# Pobieranie
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])