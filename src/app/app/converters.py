from datetime import datetime

from fastapi import APIRouter

router = APIRouter()


@router.get("/{binary}")
def convert_binary2timestampp(binary: str):
    binary = int(binary)
    stamp = datetime.fromtimestamp(binary)
    timestamp = datetime.strftime(stamp, format="%a %b %d %Y %H:%M:%S")
    return timestamp
