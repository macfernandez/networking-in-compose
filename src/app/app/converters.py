from datetime import datetime

from fastapi import APIRouter
from urllib.parse import quote 


router = APIRouter()


@router.get("/unix2datetime/{binary}")
def convert_binary2timestampp(binary: int):
    stamp = datetime.fromtimestamp(binary)
    timestamp = datetime.strftime(stamp, format="%a %b %d %Y %H:%M:%S")
    return timestamp

@router.get("/datetime2unix/{datetime}")
def convert_binary2timestampp(date: str):
    # TODO: decode date
    date = datetime.datetime.strptime(quote(datetime), "%Y-%m-%d:%H:%M:%S")
    return date.strftime("%s")
