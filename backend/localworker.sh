#! /bin/sh
if [ -d ".env" ];
then 
    echo "Enabling virtual environment"
else
    echo "No virtual environment was found"
    exit N
fi
. .env/bin/activate
export FLASK_ENV=development
celery -A main.celery worker -l info
deactivate
