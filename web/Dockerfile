FROM python:3.6-slim

COPY . /app
WORKDIR /app

RUN python -m venv /opt/venv

RUN /opt/venv/Scripts/pip pip install pip --upgrade && \
    /opt/venv/Scripts/pip install -r requirements.txt && \
    chmod +x entrypoint.sh

CMD ["/app/entrypoint.sh"]

