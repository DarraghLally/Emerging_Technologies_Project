# https://runnable.com/docker/python/dockerize-your-flask-application

MAINTANER Your Name "g00220290@gmit.ie"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "web-service.py" ]
