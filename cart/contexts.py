
def cart_count(request):

    cart = request.session.get('cart', {})
    cart_count = 0

    for id, quantity in cart.items():
        cart_count += quantity

    return {'cart_count': cart_count}