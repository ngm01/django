from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
	#validation testing...
	first_name = models.CharField(max_length=255)
	# This obviously isn't how this works...
	# def validate(first_name):
	# 	if len(first_name) < 3:
	# 		print "First name must be at least 3 characters."
	# 		return False
	last_name = models.CharField(max_length=255)
	email_address = models.CharField(max_length=255)
	age = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
