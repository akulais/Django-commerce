from __future__ import unicode_literals

from django.db import models
from datetime import datetime

class User(models.Model):
	username = models.CharField(max_length=100, default='That guy')
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.EmailField()
	password = models.CharField(max_length=100)
	class Meta:
		db_table = 'users'

class Product(models.Model):
	product_name = models.CharField(max_length=100)
	description = models.TextField()
	price = models.DecimalField(decimal_places= 2, max_digits=8)
	image_url = models.URLField(null=True, blank=True)
	quantity = models.IntegerField()
	created_at = models.DateTimeField(datetime.now())
	class Meta:
		db_table = 'products'