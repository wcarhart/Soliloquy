#!/bin/bash
set -e
set -x
git config --global core.sshCommand 'ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no'
# heroku keys:clear > /dev/null 2>&1
heroku access --app soliloquy-dev
yes | heroku keys:add > /dev/null 2>&1
git fetch > /dev/null
git checkout -b "$TRAVIS_PULL_REQUEST_BRANCH" origin/"$TRAVIS_PULL_REQUEST_BRANCH" > /dev/null 2>&1
git remote add heroku git@heroku.com:soliloquy-dev.git > /dev/null 2>&1
yes | git push heroku "$TRAVIS_PULL_REQUEST_BRANCH":master > /dev/null 2>&1
heroku run --app soliloquy-dev python manage.py makemigrations
heroku run --app soliloquy-dev python manage.py migrate
heroku run --app soliloquy-dev python architect.py
