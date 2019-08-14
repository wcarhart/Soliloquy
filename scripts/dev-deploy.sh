#!/bin/bash
set -e
git status
exit
git remote update
git fetch
git checkout "$TRAVIS_PULL_REQUEST_BRANCH"
git push soliloquy-dev "$TRAVIS_PULL_REQUEST_BRANCH":master
heroku run --app soliloquy-dev python manage.py makemigrations
heroku run --app soliloquy-dev python manage.py migrate
python architect.py
