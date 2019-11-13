FROM python:3.7-alpine

ADD . /app

RUN apk add --no-cache -Uu --virtual .build-dependencies python3-dev libffi-dev openssl-dev build-base
RUN pip install -r /app/requirements.txt

CMD ["python", "/app/main.py"]
