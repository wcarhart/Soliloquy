#!/bin/bash
set -e
set -x
yes | heroku keys:clear > /dev/null 2>&1
yes | heroku keys:add > /dev/null 2>&1
git fetch
echo "git checkout -b $TRAVIS_PULL_REQUEST_BRANCH origin/$TRAVIS_PULL_REQUEST_BRANCH"
git checkout -b "$TRAVIS_PULL_REQUEST_BRANCH" origin/"$TRAVIS_PULL_REQUEST_BRANCH"
git remote add heroku git@heroku.com:soliloquy-dev.git
git push heroku "$TRAVIS_PULL_REQUEST_BRANCH":master
heroku run --app soliloquy-dev python manage.py makemigrations
heroku run --app soliloquy-dev python manage.py migrate
python architect.py
