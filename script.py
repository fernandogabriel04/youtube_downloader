import yt_dlp

def download_youtube_video_yt_dlp(url, output_path='downloads'):
    try:
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',  # Melhor vídeo e áudio sem recompressão
            'merge_output_format': 'mp4',  # Define o formato final do arquivo como MP4
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Nome do arquivo de saída
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',  # Mescla sem reprocessamento de codec
            }],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download e mesclagem concluídos!")
        
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# URL do vídeo do YouTube que deseja baixar
video_url = input("Digite a URL do vídeo do YouTube: ")
download_youtube_video_yt_dlp(video_url)
