from django.db import models

# Create your models here.

class IMG(models.Model):
	title = models.CharField(max_length=50,default='')
	img = models.ImageField(upload_to='upload')

	def __str__(self):
		return self.title

class VID(models.Model):
	title = models.CharField(max_length=50)
	url = models.CharField(max_length=100)
	def __str__(self):
		return self.title

class ART(models.Model):
	title = models.CharField(max_length=50)
	content = models.TextField()

	def __str__(self):
		return self.title

class VIDEO(models.Model):
	title = models.CharField(max_length=50)
	vid = models.FileField(upload_to='Video')
	def __str__(self):
		return self.title

class MUS(models.Model):
	title = models.CharField(max_length=50)
	mus = models.FileField(upload_to='Music')
	def __str__(self):
		return self.title
