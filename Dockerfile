FROM python:3.7-buster
WORKDIR /app

COPY config.json /app/config.json
COPY main.py /app/spotifydl.py
COPY .env /app/.env
COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

RUN snap install -y ffmpeg

CMD ["python", "./spotifydl.py"]
