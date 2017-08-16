from django.shortcuts import render, redirect
from models import *

# Create your views here.
def index(request):
	return render(request, 'index.html', {'courses': Course.objects.all()})

def add(request):
	Course.objects.create(name=request.POST['name'], desc=request.POST['description'])
	return redirect('/')

def confirm(request, id):

	return render(request, 'confirm.html', {'course': Course.objects.get(id=id)})

def really_destroy(request, id):
	Course.objects.get(id=id).delete()
	return redirect('/')

