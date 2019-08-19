#!/bin/bash
set -e
set -x
git config --global core.sshCommand 'ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no'
yes | heroku keys:clear > /dev/null 2>&1
yes | heroku keys:add > /dev/null 2>&1
git remote add heroku git@heroku.com:soliloquy-prod.git > /dev/null 2>&1
yes | git push heroku master > /dev/null 2>&1
heroku run --app soliloquy-prod python manage.py makemigrations
heroku run --app soliloquy-prod python manage.py migrate
heroku run --app soliloquy-prod python architect.py
