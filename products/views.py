from django.views.generic import ListView
from django.shortcuts import render
from .models import Product

def products(request):
	search_param = request.GET.get('search')

	if search_param:
		products = Product.objects.filter(name__icontains = search_param)
	else:
		products = Product.objects.all()

	return render(request, 'products.html', {'products': products})


def view_product(request, id):
	product = Product.objects.get(id = id)

	return render(request, 'product_item.html', {'product': product})