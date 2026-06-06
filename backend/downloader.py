from yt_dlp import YoutubeDL

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
        ]
    }