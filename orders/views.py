from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from django.utils.decorators import method_decorator
from freelancesolution.enums import ProductType
from django.core.mail import send_mail
from django.views.generic import View
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
import stripe

# Sets the stripe API key
stripe.api_key = settings.STRIPE_SECRET

class CustomDesign(View):

	@method_decorator(login_required)
	def post(self, request):
		form = OrderForm(request.POST)
		if form.is_valid():

			# Calculate the price on the backend for security reasons
			price = 0
			if form.cleaned_data['product_type'] == ProductType.ICON.name:
				price = 75
			elif form.cleaned_data['product_type'] == ProductType.LOGO.name:
				price = 150
			elif form.cleaned_data['product_type'] == ProductType.POSTER.name:
				price = 300
			else:
				messages.error(request, "Form invalid")
				return redirect(reverse('custom_design'))

			# Get the stripe token that stripe.js put in the form before submitting
			stripe_token = request.POST.get('stripeToken')
			print(stripe_token)

			try:
				customer = stripe.Charge.create(
					amount=int(price * 100),
					currency="EUR",
					description=request.user.email,
					card=stripe_token,
				)
			except stripe.error.CardError:
				messages.error(request, "Your card was declined!")
				return redirect(reverse('custom_design'))

			if customer.paid:
				# Create the object without saving it so we can set the user
				order = form.save(commit = False)
				order.user = request.user
				order.save()

				# Send email to user
				send_mail(
					'Your new order was accepted',
					'You can view your order on your profile page. It will be delivered to you via email. Thanks for using my website!',
					'alen.krga1@gmail.com',
					[request.user.email],
					fail_silently=True,
				)

				# Send email to admin
				send_mail(
					'You have a new order',
					f'New order from {request.user.email}',
					'alen.krga1@gmail.com',
					['alen.krga1@gmail.com'],
					fail_silently=True,
				)

				messages.success(request, "You successfully requested an order. You can view it on your profile page.")
				return redirect(reverse('profile'))
			else:
				messages.error(request, "Unable to take payment")
				return redirect(reverse('custom_design'))

		else:
			messages.error(request, "Form invalid")
			return redirect(reverse('custom_design'))

	@method_decorator(login_required)
	def get(self, request):
		form = OrderForm()
		return render(request, 'custom_design.html', {'form': form, "publishable": settings.STRIPE_PUBLISHABLE})