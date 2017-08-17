from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import get_messages
from models import *
import bcrypt

# Create your views here.
def index(request):
	return render(request, 'index.html')

def register(request):
	msgs = User.objects.regValidator(request.POST)
	if len(msgs):
		for k,v in msgs.iteritems():
			print k,v
		 	messages.error(request, v, extra_tags=k)
	else:
		hashedpw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
		User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email=request.POST['email'], password=hashedpw)
		user = User.objects.last()
		request.session['logged_in'] = user.id
		print request.session['logged_in']
		return redirect('/success')

	return redirect('/')

def login(request):
	msgs = User.objects.loginValidator(request.POST)
	if len(msgs):
		print msgs
	else:
		user = User.objects.get(email=request.POST['login_email'])
		request.session['logged_in'] = user.id
		return redirect('/success')
	
	return redirect('/')

def success(request):
	if User.objects.get(id=request.session['logged_in']) == User.objects.last():
		status = "registered"
	else:
		status = "logged in"

	context = {'user': User.objects.get(id=request.session['logged_in']), 'status': status}
	return render(request, 'success.html', context)