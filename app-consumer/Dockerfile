FROM python:3.9
FROM rabbitmq

COPY . /app-consumer

WORKDIR /app-consumer

RUN apt-get update &&\
    apt-get install -y \
    python3-pip

RUN python3 -m pip uninstall pymongo
RUN python3 -m pip uninstall bson
RUN python3 -m pip install -r requirements.txt

CMD ["python3", "catalog_emit_consumer_services.py"]