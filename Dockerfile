FROM python:latest
MAINTAINER siddharth thakurdesai
RUN pip install Flask
ADD ./flask-docker.py /flask-docker.py
WORKDIR /
CMD python flask-docker.py
