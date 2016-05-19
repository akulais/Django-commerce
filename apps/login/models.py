from __future__ import unicode_literals
from django.db import models
from datetime import datetime


class User(models.Model):
	username = models.CharField(max_length=100, default='That guy')
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.EmailField()
	password = models.CharField(max_length=100)
	created_at = models.DateTimeField(default=datetime.now())

	class Meta:
		db_table = 'users'


class Product(models.Model):
	product_name = models.CharField(max_length=100)
	description = models.TextField(max_length=400)
	price = models.DecimalField(decimal_places= 2, max_digits=8)
	image_url = models.URLField(null=True, blank=True)
	quantity = models.IntegerField()
	created_at = models.DateTimeField(default=datetime.now())

	class Meta:
		db_table = 'products'


class Order(models.Model):
	product = models.ForeignKey(Product)
	user = models.ForeignKey(User)
	credit_card = models.IntegerField()
	cid_num = models.IntegerField()
	cc_exp_date = models.IntegerField()
	created_at = models.DateTimeField(default=datetime.now())

	class Meta:
		db_table = 'orders'