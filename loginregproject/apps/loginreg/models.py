from __future__ import unicode_literals

from django.db import models

import re, bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class userManager(models.Manager):
	def regValidator(self, postData):
		errors = {}
		if User.objects.filter(email = postData['email']):
		 	errors['email_exists'] = "An account associated with that email address already exists."
		if len(postData['first_name']) < 3 or not postData['first_name'].isalpha():
			errors['first_name'] = "First name must be at least 3 characters long, and use only alphabetical characters."
		if len(postData['last_name']) < 3 or not postData['last_name'].isalpha():
			errors['last_name'] = "Last name must be at least 3 characters long, and use only alphabetical characters."
		if EMAIL_REGEX.match(postData['email']) == None:
			errors['email_format'] = "Email must be in valid email format."
		if len(postData['password']) < 8:
			errors['pword_length'] = "Password must be at least 8 characters long."
		if postData['password'] != postData['pwconf']:
			errors['pwconf'] = "Password confirmation must match password."
		print errors
		return errors
	def loginValidator(self, postData):
		user = User.objects.filter(email = postData['login_email'])
		errors = {}
		if not user:
			errors['email'] = "Please enter a valid email address."
		if user and not bcrypt.checkpw(postData['login_password'].encode('utf8'), user[0].password.encode('utf8')):
			errors['password'] = "Invalid password."
		return errors

# Create your models here.
class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	objects = userManager()