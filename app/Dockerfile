FROM python:3.9
FROM rabbitmq

COPY . /app

WORKDIR /app

RUN apt-get update &&\
    apt-get install -y \
    python3-pip

RUN python3 -m pip uninstall pymongo
RUN python3 -m pip uninstall bson
RUN python3 -m pip install -r requirements.txt

EXPOSE 5000

CMD ["python3", "app.py"]