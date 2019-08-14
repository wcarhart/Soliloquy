#!/bin/bash
set -e
git checkout -b "$TRAVIS_PULL_REQUEST_BRANCH" origin/"$TRAVIS_PULL_REQUEST_BRANCH"
git push soliloquy-dev "$TRAVIS_PULL_REQUEST_BRANCH":master
heroku run --app soliloquy-dev python manage.py makemigrations
heroku run --app soliloquy-dev python manage.py migrate
python architect.py
