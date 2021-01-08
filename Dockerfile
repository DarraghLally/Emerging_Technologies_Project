# Adapted from: https://runnable.com/docker/python/dockerize-your-flask-application
# and also: Ians video on Docker

# Use this version of Python
FROM python:3.8

# change to this directory
WORKDIR /usr/src/app

# copy the requirements into the docker container (./)
COPY requirements.txt ./

# run this command in the container
# uses pip to install packages listed in requirements
# dont save temp files -> --no-cache-dir
RUN pip install --no-cache-dir -r requirements.txt

# copy everything in current folder into the container
# 1st dot is current folder, second is container
# ignores items listed in .dockerignore
COPY . .

# environment variables
ENV FLASK_APP=web-service.py

# run on
CMD flask run --host=0.0.0.0
