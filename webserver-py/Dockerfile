FROM python:3.8-slim-buster
WORKDIR /usr/src/app

# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt
COPY . . 
# start python with file on default port (8080)
CMD [ "python", "webserver.py" ]