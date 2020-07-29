from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
	name = models.CharField(max_length = 200)
	description = models.TextField()
	price = models.IntegerField(default = 0)
	img = models.ImageField(upload_to = 'products')
	high_res = models.ImageField(upload_to = 'products', null = True, blank = True)

	def __str__(self):
		return self.name


class UserProduct(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	product = models.ForeignKey(Product, on_delete = models.CASCADE)

	def __str__(self):
		return f'{self.user.username}: {self.product.name}'