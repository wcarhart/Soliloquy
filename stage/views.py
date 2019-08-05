from django.shortcuts import render
from .models import App

# Create your views here.
def stage(request):
	apps = App.objects.order_by('?')
	context = {
		'apps': apps,
	}
	return render(request, 'stage.html', context)
