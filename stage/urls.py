from django.urls import path
from . import views

urlpatterns = [
	path('', views.stage, name="stage")
]