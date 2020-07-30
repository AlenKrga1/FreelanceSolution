from django.db import models


class ContactMe(models.Model):
	email = models.CharField(max_length = 100)
	message = models.TextField()

	class Meta:
		# If not set, the admin renders it as 'Contact Mes'
		verbose_name_plural = 'Contact Me'