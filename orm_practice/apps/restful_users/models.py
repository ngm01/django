from __future__ import unicode_literals

from django.db import models


class UserManager(models.Manager):
	def validator(self, postData):
		errors = {}
		if len(postData['first_name']) < 1:
			errors['first_name'] = "Please enter a first name."
		if len(postData['last_name']) < 1:
			errors['last_name'] = "Please enter a last name."
		# need to add regex test
		if len(postData['email']) < 1:
			errors['email'] = "Please enter a valid email."

# Create your models here.
class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	# reminder: this overwrites the built-in objects key and replaces it with the "manager", which includes
	# everything that the built-in objects key (method?), along with our custom methods.
	objects = UserManager()