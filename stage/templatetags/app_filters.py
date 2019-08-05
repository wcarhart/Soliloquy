from django import template
from stage.models import App
import datetime

register = template.Library()

@register.filter(name='multiply')
def multiply(a, b):
	return a*b

@register.filter(name='mod')
def mod(dividend, divisor):
	return (dividend + 2) % divisor
	
@register.filter(name='time')
def time(creation_date):
	then = datetime.datetime.fromtimestamp(creation_date)
	now = datetime.datetime.now()
	result = (now - then).total_seconds()

	if result < 0:
		return ""

	value = 0
	quatity = ''
	if result < 60:
		value = int(result)
		quatity = 'second'
	elif result < 3600:
		value = int(result / 60)
		quatity = 'minute'
	elif result < 86400:
		value = int(result / 3600)
		quatity = 'hour'
	elif result < 604800:
		value = int(result / 86400)
		quatity = 'day'
	elif result < 2592000:
		value = int(result / 604800)
		quatity = 'week'
	elif result < 31556952:
		value = int(result / 2592000)
		quatity = 'month'
	else:
		value = int(result / 31556952)
		quatity = 'year'

	if value == 1:
		if quatity == 'day':
			return "Added yesterday"
		return f"Added {value} {quatity} ago"
	return f"Added {value} {quatity}s ago"

	