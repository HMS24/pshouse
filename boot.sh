#!/bin/bash
source venv/bin/activate

while true; do
    flask deploy
    if [[ "$?" == "0" ]]; then
        break
    fi
    echo Deploy failed, retrying in 5 secs...
    sleep 5
done

exec gunicorn -b :443 --access-logfile - --error-logfile - --keyfile ./tls/private/electricbanana.key --certfile ./tls/certs/electricbanana.crt --ca-certs ./tls/certs/electricbanana.ca-bundle pshouse:app
