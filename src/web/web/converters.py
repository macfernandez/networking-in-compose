import os
from typing import Optional

import requests

import streamlit as st


BACKEND_HOST = os.getenv("BACKEND_HOST", "127.0.0.1")
BACKEND_PORT = os.getenv("BACKEND_PORT", "8000")


def convert_unix2datetime(time_unix: str) -> Optional[str]:
    url = f"http://{BACKEND_HOST}:{BACKEND_PORT}/unix2datetime/{time_unix}"
    response = requests.get(url=url)
    if response.status_code == 200:
        st.session_state["conversion_unix2datetime"] = response.json()
    else:
        st.session_state["conversion_unix2datetime"] = "Error: No possible conversion."


def convert_datetime2unix(time_date: str, time_time: str) -> Optional[str]:
    date = time_date.strftime(format="%Y-%m-%d")
    time = time_time.strftime(format="%H:%M:%S")
    url = f"http://{BACKEND_HOST}:{BACKEND_PORT}/datetime2unix/{date}:{time}"
    response = requests.get(url=url)
    if response.status_code == 200:
        st.session_state["conversion_datetime2unix"] = response.json()
    else:
        st.session_state["conversion_datetime2unix"] = "Error: No possible conversion."
