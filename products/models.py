from django.db import models


class Product(models.Model):
	name = models.CharField(max_length = 200)
	description = models.TextField()
	price = models.IntegerField(default = 0)
	img = models.ImageField(upload_to = 'products')

	def __str__(self):
		return self.name