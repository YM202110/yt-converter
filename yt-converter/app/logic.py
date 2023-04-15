import os
import glob
from yt_dlp import YoutubeDL
from config.settings import MEDIA_ROOT, DEBUG
from django.http import FileResponse


def mp3_converter(urls):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': MEDIA_ROOT + '%(title)s.%(ext)s',
        'postprocessors': [
            {'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'},
            {'key': 'FFmpegMetadata'},
        ],
    }
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download(urls)
    except:
        return 'URLを確認してください'


def file_download(request, file_name):
    file_path = f'media/{file_name}'
    return FileResponse(open(file_path, "rb"), as_attachment=True)


def file_remove():
    files = glob.glob(f'{MEDIA_ROOT}/*.mp3')
    if not files:
        return
    for file in files:
        os.remove(file)
