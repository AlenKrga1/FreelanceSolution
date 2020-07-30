from django.shortcuts import render
from products.models import Product

# Renders the Home page
def index(request):
	products = Product.objects.all()[:3]
	return render(request, 'index.html', {'products': products})

