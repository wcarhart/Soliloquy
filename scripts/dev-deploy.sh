#!/bin/bash
set -e
git fetch
git push https://git.heroku.com/soliloquy-dev.git "$TRAVIS_PULL_REQUEST_BRANCH":master
heroku run --app soliloquy-dev python manage.py makemigrations
heroku run --app soliloquy-dev python manage.py migrate
python architect.py
