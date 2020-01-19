FROM python:3.9.0a2-alpine3.10

# Copy all files to /src
COPY . /src
WORKDIR /src

# Install requirements
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Run the app
CMD ["python", "router.py"]
