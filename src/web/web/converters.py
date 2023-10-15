import requests

import streamlit as st


def convert_unix2datetime(time_unix):
    response = requests.get(url=f"http://app:5000/{time_unix}")
    if response.status_code == 200:
        st.session_state["conversion_unix2datetime"] = response.json()
    else:
        st.session_state["conversion_unix2datetime"] = "Error: No possible conversion."

def convert_datetime2unix(time_date, time_time):
    date = time_date.strftime(format="%Y-%m-%d")
    time = time_time.strftime(format="%H:%M:%S")
    response = requests.get(url=f"http://127.0.0.1:5000/datetime2unix/{date}:{time}")
    if response.status_code == 200:
        st.session_state["conversion_datetime2unix"] = response.json()
    else:
        st.session_state["conversion_datetime2unix"] = "Error: No possible conversion."
