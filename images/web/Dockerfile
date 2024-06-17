ARG IMAGE
FROM ${IMAGE}

COPY ./src/web /tmp/web

RUN pip3 install --no-cache-dir /tmp/web

EXPOSE 8501

CMD ["streamlit", "run", "/tmp/web/web/Home.py"]
