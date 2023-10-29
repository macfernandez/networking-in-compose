ARG IMAGE

FROM ${IMAGE}

COPY ./src/app /tmp/app

RUN pip install --no-cache-dir /tmp/app

EXPOSE ${BACKEND_PORT}

CMD python3 -m app