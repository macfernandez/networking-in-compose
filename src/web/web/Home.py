import streamlit as st

from web.converters import convert_unix2datetime, convert_datetime2unix


def clean(*args) -> None:
    for a in args:
        st.session_state[a] = None


for key in ["time_unix", "time_date", "time_time", "conversion_unix2datetime", "conversion_datetime2unix"]:
    if key not in st.session_state:
        st.session_state[key] = None

st.title(":stopwatch: Convert Timestamp")

st.header(":arrow_right: From UNIX to Date and Time")
time_unix = st.text_input("Enter UNIX Time", value=None, key="time_unix")

if not st.session_state.conversion_unix2datetime:
    disabled = not bool(time_unix)
    st.button(
        label=":green[Convert]",
        on_click=convert_unix2datetime,
        args=[time_unix],
        key="convert_unix2datetime",
        disabled=disabled
    )
else:
    st.button(label=":red[Refresh]", on_click=clean, args=["time_unix", "conversion_unix2datetime"], key="clean_time_unix")
    st.write(f"Conversion: _{st.session_state.conversion_unix2datetime}_")

st.header(":arrow_right: From Date and Time to UNIX")
time_date = st.date_input("Enter a Date", value=None, key="time_date")
time_time = st.time_input("Enter a Time", value=None, key="time_time")

if not st.session_state.conversion_datetime2unix:
    disabled = not (time_date and time_time)
    st.button(
        label=":green[Convert]",
        on_click=convert_datetime2unix,
        args=[time_date, time_time],
        key="convert_datetime2unix",
        disabled=disabled
    )
else:
    st.button(label=":red[Refresh]", on_click=clean, args=["time_date","time_time","conversion_datetime2unix"])
    st.write(f"Conversion: _{st.session_state.conversion_datetime2unix}_")
