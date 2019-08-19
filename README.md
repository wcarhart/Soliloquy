# [Soliloquy](https://www.soliloquy.dev) [![Build Status](https://travis-ci.org/wcarhart/Soliloquy.svg?branch=master)](https://travis-ci.org/wcarhart/Soliloquy)
(n) an act of speaking one's thoughts aloud when by oneself or regardless of any hearers

## [Soliloquy](https://www.soliloquy.dev) is a place to display and explore cool software hobby projects.
What to submit your own project? Follow the instructions below.

## Instructions for Contributing
1. [Fork this repository](https://help.github.com/en/articles/fork-a-repo).
2. Add a new markdown (`.md`) file in `content/` for your project. Use the format described below. Name the file the name of your project (i.e. `myproject.md`). If you'd like to add a cover image for your project, add it to the `content/app_img/` folder. 
3. Open a new [pull request](https://help.github.com/en/articles/creating-a-pull-request). Once merged, your project will appear on Soliloquy!

## Formatting your Contribution Content
Use the following format when updating `template.md`:
```
name: name of your project
author: your full name
author_github: URL of your GitHub page
blurb: a short, one sentence summary of your project
description: a longer description of your project
url: URL to your deployed project
img: an icon, logo, or cover photo for your project
timestamp: today's date
```
Here's an example:
```
name: willcarh.art
author: Will Carhart
author_github: https://github.com/wcarhart
blurb: Portfolio, personal website, full-stack web app
description: As much as I hate to admit it, most average people don't get too excited about CLIs. I'm sure every developer at some point has spent weeks on a cool command line utility, only to have the uninitiated proclaim that's it? So, I decided to build willcarh.art, the world's greatest personal website, per me. And, as an aspiring Pythonista, I wrote it in Python. Please enjoy :)
url: https://www.willcarh.art
img: willcarh.art.png
timestamp: August 5th, 2019
```

## Format Restrictions
*The fields in `template.md` must adhere to the following format restrictions.*

| Field | Type | Required? | Restrictions |
|:-----:|:----:|:---------:| ------------ |
| `name` | *string* | yes | Maximum length is 100 characters |
| `author` | *string* | yes | Maximum length is 100 characters |
| `author_github` | *URL* | no | Must be a valid GitHub URL |
| `blurb` | *string* | yes | Maximum length is 100 characters |
| `description` | *string* | yes | Maximum length is 1000 characters |
| `url` | *URL* | yes | Must be a valid URL |
| `img` | *filename* | no | Must be the name of a valid image file (`.png`, `.jpg`, `.jpeg`, or `.gif`) that exists in `content/app_img/` |
| `timestamp` | *time format* | yes | Must be an unambiguous timestamp of today's date, suggested format is *Month Day, Year* |

**For optional fields, leave the value blank but still include the field name.** For example, if I don't want to include a link to my GitHub, I would use:
```
name: willcarh.art
author: Will Carhart
author_github:
...
```

**There cannot be any name conflicts between filenames.** If `project.md` already exists, you'll have to name your file `project2.md` or something like that. The same goes for image files. However, this is not the case for the actual `name` field in the content of the `.md` file, just the filename.

**Images are scaled to fit within their display cards while still maintaining their aspect ratio.** The maximum image height is 1000px (taller than 1000px will be cropped).

*These restrictions will be tested when you submit your PR by Soliloquy's CI.*

## Content Restrictions
There are a few minor content restrictions for what is allowed on Soliloquy. Read about them in the [Soliloquy FAQs](https://www.soliloquy.dev/about).
