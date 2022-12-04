import os, glob
from yt_dlp import YoutubeDL
from config.settings import MEDIA_ROOT, DEBUG
from django.http import FileResponse


def mp3_converter(urls):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': MEDIA_ROOT + '/%(title)s.%(ext)s',
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
    file_path = f'media_root/{file_name}'
    return FileResponse(open(file_path, "rb"), as_attachment=True)


def file_remove():
    files = glob.glob(f'{MEDIA_ROOT}/*.mp3')
    print(f'>>>remove MEDIA_ROOT {MEDIA_ROOT}')
    print(f'>>>remove files {files}')
    if not files:
        return
    if DEBUG:
        for file in files:
            os.remove(file)
