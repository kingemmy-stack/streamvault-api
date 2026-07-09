from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="StreamVault API",
    version="1.0.0",
    description="Video Downloader Backend"
)

# Allow requests from your PHP website
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # We'll lock this down later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "status": "online",
        "message": "Welcome to StreamVault API 🚀"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }