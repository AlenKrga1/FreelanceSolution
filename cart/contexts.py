from products.models import Product

# Called every time the template renders so the template has the cart info available every time
def cart_data(request):

	cart = request.session.get('cart', {})
	cart_count = 0
	total = 0

	# We copy the cart dictionary so we can remove items during the iteration
	for id, quantity in cart.copy().items():
		try:
			item = Product.objects.get(id = id)
			total += quantity * item.price
			cart_count += quantity
		except:
			# Product was deleted so we need to remove it from the cart
			cart.pop(id)

	request.session['cart'] = cart


	return {'cart_count': cart_count, 'total_price': total}