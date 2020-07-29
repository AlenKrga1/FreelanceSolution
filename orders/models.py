from freelancesolution.enums import ProductType
from django.contrib.auth.models import User
from django.db import models


class Order(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	description = models.TextField()
	product_type = models.CharField(max_length=15, choices=[(tag.name, tag.value) for tag in ProductType])