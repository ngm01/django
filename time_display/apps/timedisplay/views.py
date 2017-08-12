from django.shortcuts import render, HttpResponse, redirect
from time import localtime, strftime

# Create your views here.
def index(request):
	gmt = {
	'date': strftime("%b %d, %Y", localtime()),
	'time':  strftime('%#I:%M %p', localtime())
	} 
	timenow = "The time is now", gmt['time']
	print gmt['time']
	return render(request, 'timedisplay/index.html', gmt)