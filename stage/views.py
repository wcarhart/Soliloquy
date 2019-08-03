from django.shortcuts import render
from .models import App
from random import shuffle

# Create your views here.
def stage(request):
	apps = App.objects.all()
	shuffle(apps)
	context = {
		'apps': apps,
	}
	return render(request, 'stage_index.html', context)
	