FROM ubuntu

# update & install required packages
# libpq-dev & gcc required for building psycopg2
RUN apt update && apt install -y python3 python3-pip libpq-dev gcc

# copy and install requirements.txt
COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

# copy the rest of the files
COPY . .

EXPOSE 5000

ARG PYTHON_MODULE=web
ENV PYTHON_MODULE_ENV=$PYTHON_MODULE

ENTRYPOINT python3 -m $PYTHON_MODULE_ENV
