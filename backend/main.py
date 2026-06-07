from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from downloader import get_video_info, download_video
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/") # check if the server is live
def root():
    return {"message": "Saveroot API is running"}

@app.post("/info")
def fetch_info(data: dict):
    url = data["url"]
    result = get_video_info(url)
    return result

@app.post ("/download")
def fetch_download(data: dict):
    url = data["url"]
    format_id = data["format_id"]
    file_path = download_video(url, format_id)
    return FileResponse(
        path = file_path,
        filename=os.path.basename(file_path),
        media_type="application/octet-stream"
    )