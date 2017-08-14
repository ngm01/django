from django.shortcuts import render, redirect
from random import randint
from time import strftime, localtime

# Create your views here.
def index(request):
	if 'gold' not in request.session:
	 	request.session['gold'] = 0
	return render(request, 'index.html')

def process_money(request):
	if 'updates' not in request.session:
		request.session['updates'] = []

	time = strftime("%Y/%m/%d %#I:%#M %p", localtime())

	if request.POST['building'] == 'farm':
		amt = randint(10, 21)
		request.session['gold'] += amt
		data = {
		'text': "Earned {} gold from the farm!".format(amt),
		'color': 'green',
		'time': time
		}
	if request.POST['building'] == 'cave':
		amt = randint(5, 11)
		request.session['gold'] += amt
		data = {
		'text': "Earned {} gold from the cave!".format(amt),
		'color': 'green',
		'time': time
		}
	if request.POST['building'] == 'house':
		amt =  randint(2, 6)
		request.session['gold'] += amt
		data = {
		'text': "Earned {} gold from the house!".format(amt),
		'color': 'green',
		'time': time
		}
	if request.POST['building'] == 'casino':		
		amt = randint(-50, 51)
		request.session['gold'] += amt
		if amt > 0:
			data = {
			'text': "Earned {} gold from the casino!".format(amt),
			'color': 'green',
			'time': time
			}
		elif amt == 0:
			data = {
			'text': "Earned no gold from the casino.",
			'color': '',
			'time': time
			}
		else:
			data = {
			'text': "Lost {} gold at the casino. Ouch..".format(amt),
			'color': 'red',
			'time': time
			}
	request.session['updates'].append(data)
	
	return redirect('/')

def clear(request):
	request.session.clear()
	return redirect('/')