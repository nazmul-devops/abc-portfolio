FROM python:3.9-slim-bullseye

EXPOSE 8002

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y \
    postgresql-client \
    default-libmysqlclient-dev \
    build-essential \
    libpq-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev 

# Install the application server.
# RUN pip install "gunicorn==20.0.4"

# Install the project requirements.
WORKDIR /backend

COPY requirements.txt /
RUN pip install -r /requirements.txt

# COPY requirements.txt /code/
# RUN pip install -r requirements.txt
COPY . /backend/

# CMD [ "python3" , "manage.py" , "runserver" , "0.0.0.0:8000" ]