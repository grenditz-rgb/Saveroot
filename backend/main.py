from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from downloader import get_video_info

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