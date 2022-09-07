FROM python:3.8-slim

ENV FLASK_APP pshouse.py
ENV FLASK_CONFIG docker

RUN useradd admin

WORKDIR /home/admin
RUN chown -R admin:admin ./

COPY requirements requirements
RUN python3 -m venv venv
RUN venv/bin/pip3 install -r requirements/docker.txt

COPY --chown=admin:admin app app
COPY --chown=admin:admin migrations migrations
COPY --chown=admin:admin tests tests
COPY --chown=admin:admin pshouse.py config.py boot.sh ./

RUN chmod +x boot.sh

USER admin
EXPOSE 5000
