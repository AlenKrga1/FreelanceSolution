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

	products = Product.objects.filter(name__icontains = search_param, product_type__icontains = category_param)

	return render(request, 'products.html', {'products': products})


def view_product(request, id):
	product = Product.objects.get(id = id)
	reviews = ProductReview.objects.all().filter(product = product).order_by('-date_created')

	owns_product = len(UserProduct.objects.filter(user = request.user, product = product)) > 0

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

			owns_product = len(UserProduct.objects.filter(user = request.user, product = product)) > 0

			if not owns_product:
				messages.error(request, "Invalid request")
				return redirect(reverse('view_product', args=(product_id, )))

			review = form.save(commit = False)

			review.user = request.user
			review.product = product

			review.save()

		return redirect(reverse('view_product', args=(product_id, )))