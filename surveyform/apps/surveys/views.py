from django.shortcuts import render, redirect

# Create your views here.
constants = {'count': 0}
def index(request):
	return render(request, 'surveys/index.html')

def submit(request):
	if request.method=='POST':
		request.session['name'] = request.POST['name']
		request.session['language'] = request.POST['language']
		request.session['location'] = request.POST['location']
		request.session['comment'] = request.POST['comment']
	return redirect('/result')

def result(request):
	constants['count'] += 1
	return render(request, 'surveys/results.html', constants)