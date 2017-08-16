from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
	return render(request, 'index.html', {'users': User.objects.all()})

def show(request, id):
	return render(request, 'show.html', {'user': User.objects.get(id=id)})

def new(request):
	return render(request, 'add.html')

def create(request):
	User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
	return redirect('/users/{}'.format(User.objects.last().id))

def destroy(request, id):
	User.objects.get(id=id).delete()
	return redirect('/')

def edit(request, id):
	return render(request, 'edit.html', {'user': User.objects.get(id=id)})

def update(request, id):
	user = User.objects.get(id=id)
	user.first_name = request.POST['first_name']
	user.last_name = request.POST['last_name']
	user.email = request.POST['email']
	user.save()
	return redirect('/users/{}'.format(User.objects.get(id=id).id))