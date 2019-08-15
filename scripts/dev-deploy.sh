#!/bin/bash
set -e
# yes | heroku keys:clear
yes | heroku keys:add
git fetch
echo "git checkout -b $TRAVIS_PULL_REQUEST_BRANCH origin/$TRAVIS_PULL_REQUEST_BRANCH"
git checkout -b "$TRAVIS_PULL_REQUEST_BRANCH" origin/"$TRAVIS_PULL_REQUEST_BRANCH"
git push https://git.heroku.com/soliloquy-dev.git "$TRAVIS_PULL_REQUEST_BRANCH":master
heroku run --app soliloquy-dev python manage.py makemigrations
heroku run --app soliloquy-dev python manage.py migrate
python architect.py
