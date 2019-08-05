from django import template
from stage.models import App

register = template.Library()

@register.filter(name='multiply')
def multiply(a, b):
	return a*b

@register.filter(name='resolve')
def resolve(_, name):
	app = App.objects.get(name=name)
	return app.id

@register.filter(name='mod')
def mod(dividend, divisor):
	return (dividend + 2) % divisor
	