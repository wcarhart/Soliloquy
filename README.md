# [Soliloquy](https://www.soliloquy.dev)
(n) an act of speaking one's thoughts aloud when by oneself or regardless of any hearers

## Soliloquy is a place to display and explore cool software hobby projects.
#### Take a peek for yourself: https://www.soliloquy.dev
What to submit your own project? Follow the instructions below.

## Instructions for Contributing
1. [Fork this repository](https://help.github.com/en/articles/fork-a-repo).
2. Edit the file `content/template.md`. Use the format described below. When you're done, rename the file `template.md` to the name of your project (e.g. `myproject.md`). If you'd like to add a cover image for your project, add it to the `img/` folder. 
3. Open a new [pull requst](https://help.github.com/en/articles/creating-a-pull-request). Once merged, your project will appear on Soliloquy.

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

## Format restrictions
The fields in `template.md` must adhere to the following format restrictions:
* *name* **[required]** a string, maximum length is 100 characters
* *author* **[required]** a string, maximum length is 100 characters
* *author_github* **[optional]** a valid GitHub URL
* *blurb* **[required]** a string, maximum length is 100 characters
* *description* **[required]** a string, maximum length is 1000 characters
* *url* **[required]** a valid URL
* *img* **[optional]** a valid image filename for the corresponding image file in `img/` (if you do not provide an image, a default one will be provided for you)
* *timestamp* **[required]** an unambiguous timestamp of today's date, suggested format is "Month Day, Year"

These restrictions will be tested when you submit your PR by Soliloquy's CI.

## Content restrictions
There are a few minor content restrictions for what is allowed on Soliloquy. Read about them in the [Soliloquy FAQs](https://www.soliloquy.dev/about).