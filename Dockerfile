# syntax=docker/dockerfile:1
FROM alpine:3.14
RUN apk add --no-cache --update python3 py3-pip
RUN apk add py3-pandas
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD [ "python3", "main.py","--host", "0.0.0.0"]


