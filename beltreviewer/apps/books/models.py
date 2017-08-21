from __future__ import unicode_literals

from django.db import models
from ..loginreg.models import User


class Author(models.Model):
	name = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

class Book(models.Model):
	title = models.CharField(max_length=255)
	author = models.ForeignKey(Author, related_name='authorsbooks')
	uploader = models.ForeignKey(User)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

class Review(models.Model):
	review = models.TextField()
	rating = models.IntegerField()
	book = models.ForeignKey(Book, related_name = 'bookscomments')
	reviewer = models.ForeignKey(User, related_name="user_reviews")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)




	