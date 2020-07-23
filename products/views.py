from django.views.generic import ListView
from django.shortcuts import render
from .models import Product

class Products(ListView):
	template_name = 'products.html'
	model = Product
