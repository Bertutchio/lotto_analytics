## Builder
FROM python:3.8.2-alpine3.11 AS builder

WORKDIR /wheels

COPY ./requirements /wheels/requirements/
RUN pip install -U pip \
    && pip wheel -r ./requirements/app.txt \
    && pip wheel -r ./requirements/dev.txt

## Base
FROM python:3.8.2-alpine3.11 as base 

RUN mkdir /app
WORKDIR /app

COPY --from=builder /wheels /wheels
RUN pip install -U pip \
    && pip install -r /wheels/requirements/app.txt \
    -f /wheels \
    && rm -rf /wheels \
    && rm -rf /root/.cache/pip/*

## Dev
FROM base AS dev

RUN apk add git

COPY --from=builder /wheels /wheels
RUN pip install -U pip \
    && pip install -r /wheels/requirements/dev.txt \
    -f /wheels \
    && rm -rf /wheels \
    && rm -rf /root/.cache/pip/*

## Production
FROM base AS production

RUN addgroup -S python_app && \
    adduser -H -S -G python_app python_app

USER python_app

COPY  --chown=python_app:python_app entrypoint.sh /
COPY  --chown=python_app:python_app wait-for-it.sh /

ENTRYPOINT [ "/bin/ash", "entrypoint.sh" ]