from django.db import models

# Create your models here.

class profile(models.Model):

	name = models.CharField(max_length=200)
	department = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	research = models.TextField(max_length=400)
