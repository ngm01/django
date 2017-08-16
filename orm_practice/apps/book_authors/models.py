from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Author(models.Model):
	first_name = models.CharField(max_length = 255)
	last_name = models.CharField(max_length = 255)
	email = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	notes = models.TextField(default="notes")

class Book(models.Model):
	name = models.CharField(max_length = 255)
	desc = models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	authors = models.ManyToManyField(Author)