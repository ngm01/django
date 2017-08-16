from __future__ import unicode_literals

from django.db import models

class Dojos(models.Model):
	name = models.CharField(max_length=255)
	city = models.CharField(max_length=255)
	state = models.CharField(max_length=2)
	desc = models.TextField(default="Add your text here")

class Ninjas(models.Model):
	dojo = models.ForeignKey(Dojos, related_name = "ninjas")
	first_name = models.CharField(max_length = 255)
	last_name = models.CharField(max_length = 255)