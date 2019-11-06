FROM python:3.7-alpine

ADD . /app

RUN pip install -r /app/requirements.txt

CMD ["python", "/app/main.py"]
