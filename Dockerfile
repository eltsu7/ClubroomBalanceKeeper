FROM python:alpine3.10
RUN mkdir /code
WORKDIR /code

# install dependencies
RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add postgresql-dev python-dev && \
    apk add netcat-openbsd

COPY requirements.txt /code/
RUN pip3 install -r requirements.txt
COPY . /code/