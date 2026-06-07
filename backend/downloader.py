from yt_dlp import YoutubeDL
import os

def get_video_info(url: str):
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    return {
        "title": info["title"],
        "thumbnail": info["thumbnail"],
        "duration": info["duration"],
        "formats": [
            {
                "format_id": f["format_id"],
                "ext": f["ext"],
                "resolution": f.get("resolution", "audio only"),
                "filesize": f.get("filesize", None),
            }
            for f in info["formats"]
                if f.get("ext") != "mhtml"
        ]
    }

def download_video(url: str, format_id: str):
    output_dir = "downloads"
    os.makedirs(output_dir, exist_ok=True)

    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'format': format_id,
        'outtmpl': f'{output_dir}/%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
        'postprocessors': [{
            'key': 'FFmpegVideoRemuxer',
            'preferedformat': 'mp4',
        }],
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        file_path = ydl.prepare_filename(info)
        base = os.path.splitext(file_path)[0]

        for ext in ['mp4', 'mkv', 'webm', 'm4a', 'mp3']:
            candidate = f"{base}.{ext}"
            print(f"Checking: {candidate} - exists: {os.path.exists(candidate)}")
            if os.path.exists(candidate):
                return candidate
            
    return file_path