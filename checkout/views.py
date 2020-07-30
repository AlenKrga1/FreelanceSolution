from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from django.utils.decorators import method_decorator
from products.models import Product, UserProduct
from django.views.generic import View
from django.http import JsonResponse
from django.contrib import messages
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET


class Checkout(View):

	@method_decorator(login_required)
	def post(self, request):
		cart = request.session.get('cart', {})
		total = 0

		stripe_token = request.POST.get('stripeToken')
		products = []

		for id, quantity in cart.items():
			item = Product.objects.get(id = id)
			products.append(item)
			total += quantity * item.price

		try:
			customer = stripe.Charge.create(
				amount=int(total * 100),
				currency="EUR",
				description=request.user.email,
				card=stripe_token,
			)
		except stripe.error.CardError:
			messages.error(request, "Your card was declined!")

		if customer.paid:
			user_products = []

			for product in products:
				user_product = UserProduct(user = request.user, product = product)
				user_products.append(user_product)

			# Used bulk_create to optimize the DB queries
			UserProduct.objects.bulk_create(user_products)

			request.session['cart'] = {}

			messages.success(request, "Congratulations on your purchase!")

			return redirect(reverse('profile'))
		else:
			messages.error(request, "Unable to take payment")

		return render(request, 'checkout.html', {'publishable': settings.STRIPE_PUBLISHABLE})

	@method_decorator(login_required)
	def get(self, request):
		cart = request.session.get('cart', {})

		if not cart:
			return redirect(reverse('view_cart'))

		return render(request, 'checkout.html', {'publishable': settings.STRIPE_PUBLISHABLE})