from django.db import models

# Create your models here.
class App(models.Model):
	name = models.CharField(max_length=100, default='', null=True, blank=True)
	author = models.CharField(max_length=100, default='', null=True, blank=True)
	author_github = models.TextField(default='', null=True, blank=True)
	blurb = models.CharField(max_length=100, default='', null=True, blank=True)
	description = models.TextField(default='', null=True, blank=True)
	url = models.TextField(default='', null=True, blank=True)
	img = models.FilePathField(path='/img', default='', null=True, blank=True)
	timestamp = models.CharField(max_length=100, default='', null=True, blank=True)

	def __str__(self):
		return f"App ({str(self.name)})"
