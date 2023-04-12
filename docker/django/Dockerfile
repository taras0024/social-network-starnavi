FROM python:3.11.0-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update
RUN apt install netcat nano -y

RUN apt install -y vim wget
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ buster"-pgdg main | tee  /etc/apt/sources.list.d/pgdg.list
RUN apt-get update
RUN apt-get -y install postgresql-client-14

RUN mkdir SN

COPY requirements.txt /SN
RUN pip install --upgrade pip
RUN pip install -r ./SN/requirements.txt --ignore-installed --force-reinstall --upgrade --no-cache-dir

COPY . /SN
WORKDIR /SN

RUN chmod o+x ./docker/wait-for.sh

EXPOSE 8080
