ARG IMAGE

FROM ${IMAGE}

COPY ./src/app /tmp/app

RUN pip install --no-cache-dir /tmp/app

EXPOSE 5000
EXPOSE 8000

CMD ["uvicorn", "app.__main__:app", "--host", "0.0.0.0", "--port", "5000"]