import time
import yt_dlp


# ---------------------------------------
# Shared yt-dlp configuration
# ---------------------------------------

def get_ydl_opts(download=False, format_id="best"):
    opts = {
        "quiet": True,
        "no_warnings": True,
        "noplaylist": True,
        "nocheckcertificate": True,
        "socket_timeout": 30,
        "retries": 10,
        "fragment_retries": 10,
        "extract_flat": False,
        "allow_unplayable_formats": True,

        "http_headers": {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/138.0 Safari/537.36"
            )
        },

        "extractor_args": {
            "youtube": {
                "player_client": [
                    "android",
                    "web"
                ]
            }
        }
    }

    if not download:
        opts["skip_download"] = True
    else:
        opts["format"] = format_id

    return opts


# ---------------------------------------
# Extract Video Information
# ---------------------------------------

def extract_video(url: str):

    for attempt in range(2):

        try:

            with yt_dlp.YoutubeDL(get_ydl_opts()) as ydl:

                info = ydl.extract_info(
                    url,
                    download=False
                )

                formats = []

                for f in info.get("formats", []):

                    if f.get("format_id") is None:
                        continue

                    formats.append({

                        "format_id": f.get("format_id"),
                        "ext": f.get("ext"),
                        "format": f.get("format"),

                        "resolution":
                            f.get("resolution")
                            or (
                                f"{f.get('height')}p"
                                if f.get("height")
                                else "Unknown"
                            ),

                        "width": f.get("width"),
                        "height": f.get("height"),

                        "filesize": f.get("filesize"),
                        "filesize_approx": f.get("filesize_approx"),

                        "fps": f.get("fps"),

                        "quality": f.get("quality"),

                        "protocol": f.get("protocol"),

                        "vcodec": f.get("vcodec"),

                        "acodec": f.get("acodec"),

                        "abr": f.get("abr"),

                        "vbr": f.get("vbr")

                    })

                return {

                    "success": True,

                    "id": info.get("id"),

                    "title": info.get("title"),

                    "description": info.get("description"),

                    "thumbnail": info.get("thumbnail"),

                    "duration": info.get("duration"),

                    "uploader": info.get("uploader"),

                    "uploader_id": info.get("uploader_id"),

                    "view_count": info.get("view_count"),

                    "like_count": info.get("like_count"),

                    "upload_date": info.get("upload_date"),

                    "extractor": info.get("extractor"),

                    "tags": info.get("tags", []),

                    "subtitles": info.get("subtitles", {}),

                    "formats": formats

                }

        except Exception as e:

            if attempt == 1:
                return {
                    "success": False,
                    "error": str(e)
                }

            time.sleep(2)


# ---------------------------------------
# Get Direct Download URL
# ---------------------------------------

def get_download_url(url: str, format_id: str = "best"):

    for attempt in range(2):

        try:

            with yt_dlp.YoutubeDL(
                get_ydl_opts(
                    download=True,
                    format_id=format_id
                )
            ) as ydl:

                info = ydl.extract_info(
                    url,
                    download=False
                )

                return {
                    "success": True,
                    "download_url": info.get("url")
                }

        except Exception as e:

            if attempt == 1:
                return {
                    "success": False,
                    "error": str(e)
                }

            time.sleep(2)