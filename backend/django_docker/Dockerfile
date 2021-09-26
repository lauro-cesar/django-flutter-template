
###########
# BUILDER #
###########

# pull official base image
FROM python:3.8  as builder

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get -y install screen

RUN pip install --upgrade pip

# lint
RUN pip install flake8
COPY . .
RUN flake8  --ignore=E501,F401,E402 .

# install dependencies
COPY ./requirements.txt .
COPY ./requirements .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt


#########
# FINAL #
#########

# pull official base image
FROM python:3.8
RUN apt-get update && apt-get -y install postgresql-client binutils libgdal-dev libproj-dev gdal-bin postgis netcat
RUN export LC_ALL="pt_BR.UTF-8"
RUN export LC_CTYPE="pt_BR.UTF-8"
RUN dpkg-reconfigure locales


RUN apt-get update && apt-get -y install screen
ENV APP_HOME=/home/django_project

# create directory for the app user
RUN mkdir -p $APP_HOME
#RUN useradd -U -M  app
WORKDIR $APP_HOME
RUN pip install --upgrade pip
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --no-cache /wheels/*