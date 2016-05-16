from django.shortcuts import render, redirect
from django.contrib.auth import forms, login, authenticate, logout
from django.http import HttpResponse
from .forms import User_form, Auth_form, Product_form
from django.views.generic.base import TemplateView
from django.views.generic import View
from .models import Product

class User(object):
	template=''
	context = None
	user = None
	def get_template(self):
		if self.template == '':
			raise ImproperlyConfigured('Not available')
		return self.template

class Index(TemplateView):
	template = 'login/index.html'
	def get(self,request):
		form = {'form': Auth_form}
		return render(request, self.template, form)

class Login(View):
	form = Auth_form
	def get(self, request):
		context = {'form':self.form()}
		return render(request, 'login/login.html', context)
	def post(self, request):
		form = self.form(data=request.POST)
		print form.errors
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)


# NEED TO CHECK THE LOGIN(VIEW) PORTION


				# products = get_products()
				# context = { 'user' : user,
				# 	'products': products, }
				return render(request, 'login/shop.html')
			else:
				context = {'form':form}
				return render(request, 'login/login.html', context)
		else:
			return redirect('/')

class Register(TemplateView):
	form = User_form
	def get(self, request):
		context = {'form': self.form()}
		return render(request, 'login/register.html', context)
	def post(self, request):
		form = self.form(request.POST)
		if form.is_valid():
			form.save()


# NEED TO CHECK THE LOGIN(VIEW) PORTION


				# products = get_products()			context = {
			# 'products': products,
			# }	
			return render(request, 'login/shop.html')
		else:
			context = {'form':form}
			return render(request, 'login/register.html', context)

class Success(TemplateView):
	template = 'login/success.html'
	def get(self,request):
		return render(request, self.template)

# class Logout(View):
def logout(request):
	print 'loggin out'
	logout(request)
	return render(request, 'login/login.html')

def get_products(request):
	products = Product.objects.all()
	return products


#THIS IS THE START OF THE PRODUCT PORTION OF THE APP
class Product(TemplateView):
	form = Product_form
	def get(self, request):
		context = {'form':self.form()}
		return render(request, 'login/add_product.html', context)
	def post(self, request):
		form = self.form(request.POST)
		if form.is_valid():
			form.save()
			

# NEED TO CHECK THE LOGIN(VIEW) PORTION


				# products = get_products()
			# context = {
			# 'products' : products,
			# }
			return render(request, 'login/shop.html')
		else:
			context = {'form':form}
			return render(request, 'login/add_product.html', context)