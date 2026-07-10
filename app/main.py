from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.downloader import extract_video, get_download_url
from app.models import ExtractRequest, DownloadRequest

app = FastAPI(
    title="StreamVault API",
    version="2.0.0",
    description="Video Downloader Backend"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "status": "online",
        "message": "StreamVault API is running 🚀"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.post("/extract")
def extract(data: ExtractRequest):
    return extract_video(data.url)

@app.post("/download")
def download(data: DownloadRequest):
    return get_download_url(data.url, data.format)

@app.get("/version")
def version():
    return {
        "version": "2.0.0",
        "engine": "yt-dlp"
    }