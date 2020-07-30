from django.contrib.auth.decorators import login_required
from .models import Product, ProductReview, UserProduct
from django.shortcuts import render, redirect, reverse
from django.utils.decorators import method_decorator
from freelancesolution.enums import ProductType
from django.views.generic import View
from django.contrib import messages
from .forms import WriteReviewForm


def products(request):
	search_param = request.GET.get('search', '')
	category_param = request.GET.get('category', '')

	# If the GET params are '' then this query will return all products
	products = Product.objects.filter(name__icontains = search_param, product_type__icontains = category_param)

	return render(request, 'products.html', {'products': products})


def view_product(request, id):
	product = Product.objects.get(id = id)
	# Gets all product reviews and sorts them by newest
	reviews = ProductReview.objects.all().filter(product = product).order_by('-date_created')

	if request.user.is_authenticated:
	# This tells us if the user owns the product so we can determine if they can write a review
		owns_product = len(UserProduct.objects.filter(user = request.user, product = product)) > 0
	else:
		owns_product = False

	return render(request, 'product_item.html', {'product': product, 'reviews': reviews, 'owns_product': owns_product})


class WriteReview(View):

	@method_decorator(login_required)
	def get(self, request):
		form = WriteReviewForm()
		product_id = request.GET.get('id')

		return render(request, 'write_review.html', {'form': form, 'product_id': product_id})

	@method_decorator(login_required)
	def post(self, request):
		form = WriteReviewForm(request.POST)
		product_id = request.GET.get('id')

		if form.is_valid():
			try:
				product = Product.objects.get(id = product_id)
			except:
				messages.error(request, "Invalid request")
				return redirect(reverse('view_product', args=(product_id, )))

			# This tells us if the user owns the product so we can determine if they can write a review
			owns_product = len(UserProduct.objects.filter(user = request.user, product = product)) > 0

			if not owns_product:
				messages.error(request, "Invalid request")
				return redirect(reverse('view_product', args=(product_id, )))

			# Creates the object without saving so we can set user and product fields
			review = form.save(commit = False)

			review.user = request.user
			review.product = product

			review.save()

		# redirects the user to the Product details page of that particular product
		return redirect(reverse('view_product', args=(product_id, )))