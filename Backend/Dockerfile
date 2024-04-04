FROM python:3.10.9
RUN apt-get update
RUN apt-get install vim -y

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
RUN mkdir -p /app
WORKDIR /app
COPY . /app
EXPOSE 8080