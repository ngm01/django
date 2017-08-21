from django.shortcuts import render, redirect
from models import *

# Create your views here.
def index(request):
	count = 0
	latest_reviews = []
	reviews = Review.objects.order_by('-created_at')
	if reviews.count() >= 3:
		while count < 3:
			latest_reviews += [reviews[count]]
			count += 1

	print latest_reviews
	reviews = reviews.filter(created_at__lt=latest_reviews[2].created_at)

	context = {
	'user': User.objects.get(id=request.session['logged_in']),
	'reviews': reviews,
	'latest_reviews': latest_reviews
	}
	return render(request, 'books/index.html',  context)

def add(request):
	return render(request, 'books/add.html', {'authors': Author.objects.all()})

def add_this(request):
	if request.POST['new_author'] != '':
		this_author = Author.objects.create(name = request.POST['new_author'])
	else:
		this_author = Author.objects.get(name=request.POST['listed_author'])
	new_book = Book.objects.create(author=this_author, title=request.POST['title'], uploader=User.objects.get(id=request.session['logged_in']))
	Review.objects.create(review=request.POST['review'], rating=request.POST['rating'], book=new_book, reviewer=User.objects.get(id=request.session['logged_in']))
	return redirect('/')

def book(request, id):
	return render(request, 'books/book.html', {'book': Book.objects.get(id=id)})

def logout(request):
	request.session.flush()
	return redirect('/')

def users(request, id):
	return render(request, 'books/user.html', {'user': User.objects.get(id=id)})

def add_review(request):
	Review.objects.create(book = Book.objects.get(id=request.POST['book']), rating=request.POST['rating'], review=request.POST['new_review'], reviewer = User.objects.get(id=request.session['logged_in']))
	return redirect('/')