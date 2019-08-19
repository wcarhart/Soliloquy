#!/bin/bash
set -e
set -x
git config --global core.sshCommand 'ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no'
yes | heroku keys:clear > /dev/null 2>&1
yes | heroku keys:add > /dev/null 2>&1
git fetch > /dev/null
echo "git checkout -b $TRAVIS_PULL_REQUEST_BRANCH origin/$TRAVIS_PULL_REQUEST_BRANCH" > /dev/null 2>&1
git checkout -b "$TRAVIS_PULL_REQUEST_BRANCH" origin/"$TRAVIS_PULL_REQUEST_BRANCH" > /dev/null 2>&1
git remote add heroku git@heroku.com:soliloquy-dev.git > /dev/null 2>&1
yes | git push heroku "$TRAVIS_PULL_REQUEST_BRANCH":master > /dev/null 2>&1
heroku run --app soliloquy-dev python manage.py makemigrations > /dev/null 2>&1
heroku run --app soliloquy-dev python manage.py migrate > /dev/null 2>&1
heroku run --app soliloquy-dev python architect.py > /dev/null 2>&1
