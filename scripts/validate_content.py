"""
Validate the content of files included in a PR
Rules for fields:
 - name
   - required
   - type: str
   - max length: 100
 - author
   - required
   - type: str
   - max length: 100
 - author_github
   - type: str
   - must be valid URL, non 4xx and 5xx HTTP response
   - must contain substring 'github.com'
 - blurb
   - required
   - type: str
   - max length: 100
 - description
   - required
   - type: str
   - max length: 1000
 - url
   - required
   - type: str
   - must be valid URL, non 4xx and 5xx HTTP response
 - img
   - type: str
   - must be unique among all images
     - images in content/app_img/
   - must not be a prohibited image name
     - images in img/ (a few reserved image names)
   - image file must exist in content/app_img/
 - timestamp
   - required
   - type: str
   - must be unambiguous time stamp

Other rules:
 - no invalid fields (file not listed above)
"""
import re
import os
import glob
import json
import requests
import datetime
import argparse
import parsedatetime

class ContentError(object):
	def __init__(self, status_code=1, filename="", field="", short_message="", long_message=""):
		self.status_code = status_code
		self.filename = filename
		self.field = field
		self.short_message = short_message
		self.long_message = long_message

def cleanse(s):
	return s.strip('"').strip("'").strip('\n').strip(' ')

def validate_content(file, content_dir):
	"""
	Validate content for a file based on the rules listed in __doc__
		:file: (str) the name of the content file to validate
	"""
	with open(file, 'r') as f:
		file_contents = [content.replace('\n', '') for content in f.readlines()]

	contents = {}
	for line in file_contents:
		items = line.split(':')
		field, value = cleanse(items[0]), cleanse(':'.join(items[1:]))
		contents[field] = value

	status_code = 0
	filename = file
	field = ""
	short_message = ""
	long_message = "n/a"

	loop = True
	while(loop):
		loop = False
	
		# validate name
		field = 'name'
		if not 'name' in contents:
			status_code = 1
			short_message = "missing required field `name`"
			break
		if contents['name'] == '':
			status_code = 1
			short_message = "empty required field `name`"
			break
		if not str(contents['name']):
			status_code = 1
			short_message = "invalid field: `name`"
			break
		if not len(contents['name']) <= 100:
			status_code = 1
			short_message = "length of field `name` exceeds 100 characters"
			break

		# validate author
		field = 'author'
		if not 'author' in contents:
			status_code = 1
			short_message = "missing required field `author`"
			break
		if contents['author'] == '':
			status_code = 1
			short_message = "empty required field `author`"
			break
		if not str(contents['author']):
			status_code = 1
			short_message = "invalid field `author`"
			break
		if not len(contents['author']) <= 100:
			status_code = 1
			short_message = "length of field `author` exceeds 100 characters"
			break

		# validate author_github
		field = 'author_github'
		author_github = contents.get('author_github', '')
		if not author_github == '':
			if not str(author_github):
				status_code = 1
				short_message = "invalid field `author_github`"
				break
			if not 'github.com' in author_github:
				status_code = 1
				short_message = "field `author_github` must be a GitHub URL"
				break
			try:
				response = requests.get(author_github, timeout=15)
				if not response:
					status_code = 1
					short_message = "URL provided for field `author_github` returned an error HTTP code when accessed"
					long_message = f"The result of accessing \"{contents['author_github']}\" resulted in an HTTP response code of `{response.status_code}`, which is an error."
					break
			except Exception as e:
				status_code = 1
				short_message = "URL provided for field `author_github` is inaccessible"
				long_message = f"Trying to access \"{contents['author_github']}\" resulted in an unknown exception, likely indicating that the URL is invalid."
				break

		# validate blurb
		field = 'blurb'
		if not 'blurb' in contents:
			status_code = 1
			short_message = "missing required field `blurb`"
			break
		if contents['blurb'] == '':
			status_code = 1
			short_message = "empty required field `blurb`"
			break
		if not str(contents['blurb']):
			status_code = 1
			short_message = "invalid field `blurb`"
			break
		if not len(contents['blurb']) <= 100:
			status_code = 1
			short_message = "length of field `blurb` exceeds 100 characters"
			break

		# validate description
		field = 'description'
		if not 'description' in contents:
			status_code = 1
			short_message = "missing required field `description`"
			break
		if contents['description'] == '':
			status_code = 1
			short_message = "empty required field `description`"
			break
		if not str(contents['description']):
			status_code = 1
			short_message = "invalid field `description`"
			break
		if not len(contents['description']) <= 1000:
			status_code = 1
			short_message = "length of field `description` exceeds 1000 characters"
			break

		# validate url
		field = 'url'
		if not 'url' in contents:
			status_code = 1
			short_message = "missing required field `url`"
			break
		if contents['url'] == '':
			status_code = 1
			short_message = "empty required field `url`"
			break
		if not str(contents['url']):
			status_code = 1
			short_message = "invalid field `url`"
			break
		try:
			response = requests.get(contents['url'], timeout=15)
			if not response:
				status_code = 1
				short_message = "URL provided for field `url` returned an error"
				long_message = f"The result of accessing \"{contents['url']}\" resulted in an HTTP response code of `{response.status_code}`, which is an error."
				break
		except Exception as e:
			status_code = 1
			short_message = "URL provided for field `url` is inaccessible"
			long_message = f"Trying to access \"{contents['url']}\" resulted in an unknown exception, likely indicating that the URL is invalid."
			break

		# validate img
		field = 'img'
		img = contents.get('img', '')
		if not img == '':
			reserved_file_names = ['about', 'default', 'willcarhartportfolio']
			supported_filetypes = ['.png', '.jpg', '.jpeg', '.gif']
			image_filename, filetype = os.path.splitext(img)
			if not filetype in supported_filetypes:
				status_code = 1
				short_message = f"Value of field `img` file type not supported (`{filetype}`)"
				long_message = "Supported image file types are `.png`, `.jpg`, `.jpeg`, and `.gif`."
				break
			if image_filename in reserved_file_names:
				status_code = 1
				short_message = f"filename provided for field `img` is prohibited (`{image_filename}`)"
				long_message = "Some filenames are reserved for the system, as they are used elsewhere in Soliloquy's assets and thus are prohibited for use in names of contribution images. These filenames are `about`, `default`, and `willcarhartportfolio`, extension agnostic."
				break
			if not os.path.isfile(f'{content_dir}/app_img/{img}'):
				status_code = 1
				short_message = f"filename provided for field `img` not found, no such file `{os.path.basename(content_dir)}/app_img/{img}`"
				long_message = f"Make sure to add your image file to `{os.path.basename(content_dir)}/app_img/`, as this is where Soliloquy will look for it."
				break

		# validate timestamp
		field = 'timestamp'
		if not 'timestamp' in contents:
			status_code = 1
			short_message = "missing required field `timestamp`"
			break
		if contents['timestamp'] == '':
			status_code = 1
			short_message = "empty required field `timestamp`"
			break
		if any(re.match(regex, contents['timestamp']) for regex in ['../../.*', '.*/../..', '..-..-.*', '.*-..-..']):
			status_code = 1
			short_message = "value provided for field `timestamp` is ambiguous"
			long_message = f"The timestamp you provided (`{contents['timestamp']}`) is ambiguous. This means that its value is not deterministic. For example, **\"05/06/2018\"** could be interpreted as **May 6th, 2018** or **June 5th, 2018**."
			break
		try:
			parse = parsedatetime.Calendar()
			time_struct, parse_status = parse.parse(value)
			if not parse_status == 1:
				status_code = 1
				short_message = f"invalid field `timestamp`"
				long_message = f"The provided timestamp `{contents['timestamp']}` could not be parsed. Try using the format **Month Day, Year**, like August 7th, 2019."
				break
			dt = datetime.datetime(*time_struct[:6])
			timestamp = dt.timestamp()
		except ValueError:
			status_code = 1
			short_message = "invalid field `timestamp`"
			long_message = f"The provided timestamp `{contents['timestamp']}` could not be parsed. Try using the format **Month Day, Year**, like August 7th, 2019."
			break

	return ContentError(
		status_code=status_code,
		filename=os.path.basename(filename),
		field=field,
		short_message=short_message,
		long_message=long_message
	)

def update_template(template, result):
	with open(template, 'r') as f:
		contents = f.read()

	for var in vars(result).keys():
		contents = contents.replace(f'{{{{ {var} }}}}', str(getattr(result, var)))

	return contents

def update_github(travis_repo_slug, travis_pull_request, results):
	for result in results:
		if result.status_code == 1:
			payload = update_template('error.md', result)
		else:
			payload = update_template('success.md', result)

	GAUTH = os.environ.get('GAUTH')
	headers = { 'Authorization': f'token {GAUTH}' }
	content = { 'body': f'{payload}' }
	requests.post(
		f'https://api.github.com/repos/{travis_repo_slug}/issues/{travis_pull_request}/comments',
		headers=headers,
		data=content
	)
	print(payload)

def build_parser():
	parser = argparse.ArgumentParser(description=__doc__, formatter_class = argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('--travis-repo-slug', type=str, required=True)
	parser.add_argument('--travis-pull-request', type=int, required=True)
	return parser

def main():
	parser = build_parser()
	args = parser.parse_args()

	content_dir = os.path.abspath('../content/')
	files = glob.glob(f'{content_dir}/*.md')
	if 'template.md' in files:
		del files['template.md']

	results = [validate_content(file, content_dir) for file in files]
	update_github(args.travis_repo_slug, args.travis_pull_request, results)

if __name__ == '__main__':
	main()
