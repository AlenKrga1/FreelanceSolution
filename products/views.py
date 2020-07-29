from .models import Product, ProductReview, UserProduct
from freelancesolution.enums import ProductType
from django.views.generic import ListView
from django.shortcuts import render

def products(request):
	search_param = request.GET.get('search', '')
	category_param = request.GET.get('category', '')

	products = Product.objects.filter(name__icontains = search_param, product_type__icontains = category_param)

	return render(request, 'products.html', {'products': products})


def view_product(request, id):
	product = Product.objects.get(id = id)
	reviews = ProductReview.objects.all().filter(product = product)

	owns_product = len(UserProduct.objects.filter(user = request.user, product = product)) > 0

	return render(request, 'product_item.html', {'product': product, 'reviews': reviews, 'owns_product': owns_product})