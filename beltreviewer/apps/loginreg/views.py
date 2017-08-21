from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import get_messages
from models import *
import bcrypt

# Create your views here.
def index(request):
	if 'logged_in' not in request.session:
		return render(request, 'index.html')
	else:
		return redirect('/books')

def register(request):
	msgs = User.objects.regValidator(request.POST)
	if len(msgs):
		for k,v in msgs.iteritems():
			print k,v
		 	messages.error(request, v, extra_tags=k)
	else:
		hashedpw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
		User.objects.create(name = request.POST['name'], user_name=request.POST['user_name'], password=hashedpw)
		user = User.objects.last()
		request.session['logged_in'] = user.id
		print request.session['logged_in']
		return redirect('/success')

	return redirect('/')

def login(request):
	msgs = User.objects.loginValidator(request.POST)
	if len(msgs):
		for k,v in msgs.iteritems():
			print k,v
		 	messages.error(request, v, extra_tags=k)
	else:
		user = User.objects.get(user_name=request.POST['login_user_name'])
		request.session['logged_in'] = user.id
		return redirect('/success')
	
	return redirect('/')

def success(request):
	return redirect('/books')