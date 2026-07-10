import yt_dlp
import time


def extract_video(url: str):
    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        "skip_download": True,
        "noplaylist": True,

        # Better YouTube compatibility
        "extractor_args": {
            "youtube": {
                "player_client": ["android", "web"]
            }
        },

        "socket_timeout": 30,
        "retries": 10,
        "fragment_retries": 10,
        "nocheckcertificate": True
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(
                url,
                download=False,
                process=True
            )

            formats = []

            for f in info.get("formats", []):
                if not f.get("url"):
                    continue

                formats.append({
                    "format_id": f.get("format_id"),
                    "ext": f.get("ext"),
                    "resolution": f.get("resolution") or f"{f.get('height','')}p",
                    "filesize": f.get("filesize"),
                    "fps": f.get("fps"),
                    "vcodec": f.get("vcodec"),
                    "acodec": f.get("acodec")
                })

            return {
                "success": True,
                "title": info.get("title"),
                "thumbnail": info.get("thumbnail"),
                "duration": info.get("duration"),
                "uploader": info.get("uploader"),
                "view_count": info.get("view_count"),
                "formats": formats
            }

    except Exception:
        # Retry once after a short delay
        time.sleep(2)

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)

                formats = []

                for f in info.get("formats", []):
                    if not f.get("url"):
                        continue

                    formats.append({
                        "format_id": f.get("format_id"),
                        "ext": f.get("ext"),
                        "resolution": f.get("resolution") or f"{f.get('height','')}p",
                        "filesize": f.get("filesize"),
                        "fps": f.get("fps"),
                        "vcodec": f.get("vcodec"),
                        "acodec": f.get("acodec")
                    })

                return {
                    "success": True,
                    "title": info.get("title"),
                    "thumbnail": info.get("thumbnail"),
                    "duration": info.get("duration"),
                    "uploader": info.get("uploader"),
                    "view_count": info.get("view_count"),
                    "formats": formats
                }

        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }


def get_download_url(url: str, format_id: str = "best"):
    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        "format": format_id,

        "extractor_args": {
            "youtube": {
                "player_client": ["android", "web"]
            }
        },

        "socket_timeout": 30,
        "retries": 10,
        "fragment_retries": 10,
        "nocheckcertificate": True
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(
                url,
                download=False,
                process=True
            )

            return {
                "success": True,
                "download_url": info["url"]
            }

    except Exception:
        time.sleep(2)

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)

                return {
                    "success": True,
                    "download_url": info["url"]
                }

        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }