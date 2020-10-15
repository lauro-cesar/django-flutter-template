
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
RUN pip install --upgrade pip

# lint
RUN pip install flake8
COPY . .
RUN flake8  --ignore=E501,F401 .

# install dependencies
COPY ./requirements.txt .
COPY ./requirements .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt


#########
# FINAL #
#########

# pull official base image
FROM python:3.8
ENV APP_HOME=/home/backend-api
# create directory for the app user
RUN mkdir -p $APP_HOME



# create the app user
RUN addgroup app &>/dev/null
RUN adduser app



# create the appropriate directories
# RUN mkdir -p $APP_HOME/static
# RUN mkdir -p $APP_HOME/media
RUN apt-get update && apt-get -y install binutils libgdal-dev libproj-dev gdal-bin postgis

WORKDIR $APP_HOME


COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --no-cache /wheels/*

COPY . $APP_HOME

RUN chown -R app:app $APP_HOME
RUN chmod 755 $APP_HOME/entrypoint.sh
USER app

ENTRYPOINT ["/home/backend-api/entrypoint.sh"]
