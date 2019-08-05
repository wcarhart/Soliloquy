from django.shortcuts import render
from .models import App

# Create your views here.
def stage(request):
	apps = App.objects.order_by('?')
	colors = [
		'#EAC435',
		'#345995',
		'#03CEA4',
		'#FB4D3D',
		'#CA1551',
	]
	context = {
		'apps': apps,
		'colors': colors,
	}
	return render(request, 'stage.html', context)

def about(request):
	return render(request, 'about.html', {})
	