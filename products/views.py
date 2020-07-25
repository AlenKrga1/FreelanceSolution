from django.views.generic import ListView
from django.shortcuts import render
from .models import Product

class Products(ListView):
	template_name = 'products.html'
	model = Product

def view_product(request, id):
	product = Product.objects.get(id = id)

	return render(request, 'product_item.html', {'product': product})