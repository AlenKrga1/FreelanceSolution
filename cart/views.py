from django.shortcuts import render, redirect, reverse
from products.models import Product

def view_cart(request):
	cart = request.session.get('cart', {})
	cart_items = []

	for id, quantity in cart.items():
		item = Product.objects.get(id = int(id))
		cart_items.append({'product': item, 'quantity': quantity})

	return render(request, 'cart.html', {'cart_items': cart_items})


def add_to_cart(request, id):
	cart = request.session.get('cart', {})
	quantity = int(request.POST.get('quantity', 1))

	if id in cart:
		cart[id] = int(cart[id]) + quantity
	else:
		cart[id] = cart.get(id, quantity)

	request.session['cart'] = cart
	return redirect(reverse('products'))


def adjust_cart(request, id):
	quantity = int(request.POST.get('quantity', 0))
	cart = request.session.get('cart', {})

	if quantity > 0:
		cart[id] = quantity
	else:
		cart.pop(id)

	request.session['cart'] = cart

	return redirect(reverse('view_cart'))


def delete_item_from_cart(request, id):
	cart = request.session.get('cart', {})

	cart.pop(id)

	request.session['cart'] = cart

	return redirect(reverse('view_cart'))