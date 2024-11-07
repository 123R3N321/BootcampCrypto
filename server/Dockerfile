# 1 image choice. Changed from 3.7 to 3.10 to match my local
FROM python:3.10

# 2 copy the requirements.txt from the root dir into the container
COPY requirements.txt /app/
# copy all files inside the host server/ dir into the app/ dir in container
COPY src/ /app/
# set working dir in the container
WORKDIR /app
# 3 install the dependencies
RUN pip install -r requirements.txt

# 5 cloud run expects port 8080
ENV PORT 8080

# 6 run gunicorn bound to port 8080
#CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app
CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --log-level debug app:app

