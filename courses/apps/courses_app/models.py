from __future__ import unicode_literals

from django.db import models

# Create your models here.
class courseManager(models.Manager):
	def validator(self, postData):
		errors = {}

		# Stuff

		return errors

class Course(models.Model):
	name = models.CharField(max_length=255)
	desc = models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = courseManager()