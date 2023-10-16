from datetime import datetime

from fastapi import APIRouter
from urllib.parse import unquote


router = APIRouter()


@router.get("/unix2datetime/{binary}")
def convert_binary2timestampp(binary: int) -> str:
    stamp = datetime.fromtimestamp(binary)
    timestamp = datetime.strftime(stamp, format="%a %b %d %Y %H:%M:%S")
    return timestamp

@router.get("/datetime2unix/{date}")
def convert_timestamp2binary(date: str) -> str:
    date = datetime.strptime(unquote(date), "%Y-%m-%d:%H:%M:%S")
    return date.strftime("%s")
