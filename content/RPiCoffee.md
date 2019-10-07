name: RPiCoffee  
author: Michael Steudter  
author_github: https://github.com/misteu/  
blurb: Hacked Delonghi coffee machine for control via web app
description: I hacked my coffee machine to control all buttons of the front panel via a local web app. The pushbuttons can be overridden with a custom PCB I designed, that is controlled with raspberry GPIOs. A simple Python script is running on the RPIs to make the GPIOs accessible via HTTP-requests. I ended up with a responsive web app and a fancy UI including weather forecasts and a public transport API. There was some experimental stuff implemented just for fun like a mongoDB running (very slowly) on the RPi for logging purposes and bitcoin miner 🙈. I used Python and Flask with Jinja to render the web app and gpiozero to control the coffee machine via the GPIO outputs.
url: https://misteu.github.io/RPiCoffee/ 
img: interface+RPi_full.jpg 
timestamp: October 6th 2019
