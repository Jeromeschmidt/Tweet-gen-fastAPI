FROM python:latest

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY app/ /app

WORKDIR /app

CMD ["python3", "main.py"]
