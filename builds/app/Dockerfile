FROM python:3.8-slim

ARG gunicorn_options

ENV GUNICORN_OPTIONS $gunicorn_options
ENV FLASK_APP presale.py
ENV FLASK_CONFIG docker

RUN useradd presale

WORKDIR /home/presale

COPY requirements requirements
RUN python3 -m venv venv
RUN venv/bin/pip3 install -r requirements/docker.txt

COPY app app
COPY migrations migrations
COPY presale.py config.py boot.sh ./

RUN chmod +x boot.sh
RUN chown -R presale:presale ./
USER presale

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
