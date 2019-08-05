from django.urls import path
from . import views

urlpatterns = [
	path('', views.stage, name='stage'),
	path('about/', views.about, name='about'),
]