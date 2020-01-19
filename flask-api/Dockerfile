FROM python:3-alpine

# Copy all files to /src
COPY . /src
WORKDIR /src

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
    
# Install requirements
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

# Run the app
CMD ["python", "router.py"]
