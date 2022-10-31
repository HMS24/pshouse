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

exec gunicorn -b :80 --access-logfile - --error-logfile - pshouse:app
