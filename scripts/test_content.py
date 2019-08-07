import re
import os
import glob
import requests
import datetime
import parsedatetime

def cleanse(s):
	return s.strip('"').strip("'").strip('\n').strip(' ')

def validate_content(file, content_dir):
	"""
	Validate the following rules for a file
		:file: (str) the name of the content file to validate

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
	with open(file, 'r') as f:
		file_contents = [content.replace('\n', '') for content in f.readlines()]

	contents = {}
	for line in file_contents:
		items = line.split(':')
		field, value = cleanse(items[0]), cleanse(':'.join(items[1:]))
		contents[field] = value
	
	# validate name
	assert 'name' in contents, "Missing required field: 'name'"
	assert str(contents['name']), "Invalid field: 'name'"
	assert len(contents['name']) <= 100, "Length of field 'name' exceeds 100 characters"

	# validate author
	assert 'author' in contents, "Missing required field: 'author'"
	assert str(contents['author']), "Invalid field: 'author'"
	assert len(contents['author']) <= 100, "Length of field 'author' exceeds 100 characters"

	# validate author_github
	author_github = contents.get('author_github', '')
	if not author_github == '':
		assert str(author_github), "Invalid field: 'author_github'"
		assert 'github.com' in author_github, "Field 'author_github must be a GitHub URL"
		assert requests.get(author_github), "URL provided for field 'author_github' returned an error HTTP code when accessed"

	# validate blurb
	assert 'blurb' in contents, "Missing required field: 'blurb'"
	assert str(contents['blurb']), "Invalid field: 'blurb'"
	assert len(contents['blurb']) <= 100, "Length of field 'blurb' exceeds 100 characters"

	# validate description
	assert 'description' in contents, "Missing required field: 'description'"
	assert str(contents['description']), "Invalid field: 'description'"
	assert len(contents['description']) <= 1000, "Length of field 'description' exceeds 1000 characters"

	# validate url
	assert 'url' in contents, "Missing required field: 'url'"
	assert str(contents['url']), "Invalid field: 'url'"
	assert requests.get(contents['url']), "URL provided for field 'url' returned an error HTTP code when accessed"

	# validate img
	img = contents.get('img', '')
	if not img == '':
		reserved_file_names = ['about', 'default', 'willcarhartportfolio']
		filename, _ = os.path.splitext(img)
		assert not filename in reserved_file_names, "Filename provided for field 'img' is prohibited"
		assert os.path.isfile(f'{content_dir}/app_img/{img}'), f"Filename provided for field 'img' not found, no such file '{content_dir}/app_img/{img}'"

	# validate timestamp
	assert 'timestamp' in contents, "Missing required field: 'timestamp'"
	assert not any(
		re.match(regex, contents['timestamp'])
		for regex in [
			'../../.*',
			'.*/../..',
			'..-..-.*',
			'.*-..-..',
		]
	), "Value provided for field 'timestamp' is ambiguous"
	try:
		parse = parsedatetime.Calendar()
		time_struct, parse_status = parse.parse(value)
		assert parse_status == 1, f"Invalid field 'timestamp'"
		dt = datetime.datetime(*time_struct[:6])
		timestamp = dt.timestamp()
	except ValueError:
		assert True is False, "Invalid field 'timestamp'"

def main():
	content_dir = os.path.abspath('../content/')
	files = glob.glob(f'{content_dir}/*.md')
	for file in files:
		print(f"Validating {file}...")
		validate_content(file, content_dir)

if __name__ == '__main__':
	main()
