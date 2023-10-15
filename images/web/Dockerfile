ARG IMAGE
FROM ${IMAGE}

COPY /src/web /tmp/web

RUN python3 -m venv venv \
    && source venv/bin/activate

RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir /tmp/web


CMD ["streamlit", "-m", "web.Home"]
