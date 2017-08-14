from django.shortcuts import render, redirect
from time import strftime, localtime

# Create your views here.
def index(request):
	return render(request, 'session_words/index.html')

def addwords(request):
	if request.method == 'POST':
		wordtime = strftime('%#H:%M:%S%p, %B %#d %Y', localtime())
		if 'words' not in request.session:
			request.session['words'] = []
		if 'bigfont' in request.POST:
			data = {'word': request.POST['addword'],
			'color': request.POST['color'],
			'font': 'big',
			'time': wordtime}
		else:
			data = {'word': request.POST['addword'],
			'color': request.POST['color'],
			'font': 'small',
			'time': wordtime}
		request.session['words'].append(data)
		request.session.modified = True
		
		print request.session['words']
		#YOU DON'T NEED TO PASS REQUEST INTO THE REDIRECT
	return redirect('/')

def clear(request):
	request.session.clear()
	return redirect('/')