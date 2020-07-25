from products.models import Product

def cart_data(request):

	cart = request.session.get('cart', {})
	cart_count = 0
	total = 0

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