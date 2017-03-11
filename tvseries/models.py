from django.db import models
from django.contrib.auth.models import User

class Serie(models.Model):
	title = models.CharField(max_length=100, blank=True, default='')
	country = models.CharField(max_length=100, blank=True, default='')
	tvpartners = models.CharField(max_length=100, blank=True, default='')
	language = models.CharField(max_length=100, blank=True, default='')
	summary = models.TextField()
	premiered = models.DateField()
	runtime = models.IntegerField()
	genres = models.CharField(max_length=100, blank=True, default='')
	status = models.CharField(max_length=100, blank=True, default='')
	image_med = models.URLField()
	image_org = models.URLField()
	imdblink = models.URLField()
	raiting = models.FloatField()
	owner = models.ManyToManyField(User,related_name="seria")


	def __str__(self):
		return "%s" % (self.title)
