FROM python:3.8.1-slim

RUN apt-get update && \
    apt-get upgrade

RUN pip install --upgrade pip

RUN pip install elasticsearch && \
    pip install beautifulsoup4

RUN adduser --disabled-password python_app
USER python_app

WORKDIR /home/python_app/

COPY --chown=python_app:python_app entrypoint.sh .
COPY --chown=python_app:python_app wait-for-it.sh .

RUN chmod +x wait-for-it.sh

RUN mkdir -p /home/python_app/app

ENTRYPOINT [ "/bin/bash", "entrypoint.sh"]