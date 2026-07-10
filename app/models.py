from pydantic import BaseModel, HttpUrl
from typing import Optional


class ExtractRequest(BaseModel):
    url: HttpUrl


class DownloadRequest(BaseModel):
    url: HttpUrl
    format: Optional[str] = "best"