"""
Utility for converting markdown files from content/ to App model
instances in the database
"""
from django.conf import settings
import django

from soliloquy.settings import DATABASES, INSTALLED_APPS
settings.configure(DATABASES=DATABASES, INSTALLED_APPS=INSTALLED_APPS)
django.setup()

import os
import glob
from stage.models import App

import sys

def cleanse(s):
	return s.strip('"').strip("'").strip('\n').strip(' ')

def build_app(file):
	with open(file, 'r') as f:
		contents = [content.replace('\n', '') for content in f.readlines()]

	name = author = blurb = description = link = img = ''
	for line in contents:
		if line == '---' or line == '':
			continue

		items = line.split(':')
		field, value = cleanse(items[0]), cleanse(''.join(items[1:]))

		if field == 'name':
			name = value
		elif field == 'author':
			author = value
		elif field == 'blurb':
			blurb = value
		elif field == 'description':
			description = value
		elif field == 'link':
			link = value
		elif field == 'img':
			img = value
		else:
			return None

	if not all([name, author, blurb, description, link, img]):
		return None
	app = App(
		name=name,
		blurb=blurb,
		description=description,
		link=link,
		img=img
	)
	return app

def build_all_apps(source='content'):
	source = f'stage/{source}'
	if not os.path.isdir(source):
		return None

	files = glob.glob(f'{source}/*.md')
	if len(files) == 0:
		return None

	apps = []
	for file in files:
		app = build_app(file)
		if not app == None:
			apps.append(app)

	return apps

if __name__ == '__main__':
	apps = build_all_apps()
	print(apps)
