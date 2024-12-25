FROM python:alpine

WORKDIR /usr/src/app

RUN apk add --no-cache gcc musl-dev libffi-dev

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .