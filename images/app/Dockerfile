ARG IMAGE

FROM ${IMAGE}

ARG BACKEND_PORT

COPY ./src/app /tmp/app

RUN pip install --no-cache-dir /tmp/app

EXPOSE ${BACKEND_PORT}

CMD ["uvicorn", "app.__main__:app", "--host", "0.0.0.0", "--port", "5000"]