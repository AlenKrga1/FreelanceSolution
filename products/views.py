from freelancesolution.enums import ProductType
from django.views.generic import ListView
from django.shortcuts import render
from .models import Product

def products(request):
	search_param = request.GET.get('search', '')
	category_param = request.GET.get('category', '')

	products = Product.objects.filter(name__icontains = search_param, product_type__icontains = category_param)

	return render(request, 'products.html', {'products': products})


def view_product(request, id):
	product = Product.objects.get(id = id)

	return render(request, 'product_item.html', {'product': product})