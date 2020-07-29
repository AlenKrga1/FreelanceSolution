from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from django.utils.decorators import method_decorator
from freelancesolution.enums import ProductType
from django.views.generic import View
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
import stripe

stripe.api_key = settings.STRIPE_SECRET

class CustomDesign(View):

	@method_decorator(login_required)
	def post(self, request):
		form = OrderForm(request.POST)
		if form.is_valid():
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
				order = form.save(commit = False)
				order.user = request.user
				order.save()

				# Send email to user
				# Send email to admin

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