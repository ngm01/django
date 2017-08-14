from django.shortcuts import render, redirect

# Create your views here.

items = {'1001': 19.99,
		 '1002': 24.99,
		 '1003': 4.99,
		 '1004': 49.99
}

def index(request):
	return render(request, 'index.html')

def buy(request):
	request.session['purchase'] = items[request.POST['product_id']] * int(request.POST['quantity'])

	if 'item_count' not in request.session:
		request.session['item_count'] = 0
	if 'total_spent' not in request.session:
		request.session['total_spent'] = 0

	request.session['item_count'] += int(request.POST['quantity'])
	request.session['total_spent'] += float(request.session['purchase'])
	return redirect('/checkout')

def checkout(request):
	return render(request, 'checkout.html')

def clear(request):
	request.session.clear()
	return redirect('/')