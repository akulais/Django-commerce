from django.shortcuts import render, redirect
from django.contrib.auth import forms, login, authenticate, logout
from django.http import HttpResponse, Http404
from .forms import User_form, Auth_form, Product_form, Order_form
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import View
from .models import Product, Order

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
	products = Product.objects.all()

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
				context = { 'user' : user,
					'products' : self.products 
					}
				return render(request, 'login/shop.html', context)
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
			print form.errors
			form.save()
			return render(request, 'login/shop.html')
		else:
			context = {'form':form}
			return render(request, 'login/register.html', context)


class Success(TemplateView):
	template = 'login/success.html'
	def get(self,request):
		return render(request, self.template)


def logout(request):
	print 'loggin out'
	logout(request)
	return redirect('/')


class Show_Product(DetailView):
	model = Product
	template_name = 'login/display_product.html'
	form = Order_form
	

	def get_context_data(self,**kwargs):
		context = super(Show_Product, self).get_context_data(**kwargs)
		return context

	def post(self,request):
		print 'show product post'
		form = self.form(request.POST)
		print 'show product order_form'
		# form = self./form

		if form.is_valid():
			print 'form is valid'
			form.save()
			print 'form is saved'
			return render(request, 'login/shop.html')
		else:
			print form.errors
			context = {'form':form}
			print 'form has errors'
			return render(request, 'login/display_product.html', context)


class Show_Products(ListView):
	form = Product_form
	model = Product
	template_name = 'login/add_product.html'

	def get(self, request):
		context = {'form':self.form()}
		return render(request, 'login/add_product.html', context)

	def get_context_data(self,**kwargs):
		context = super(Show_Products, self).get_context_data(**kwargs)
		return context

	def post(self, request):
		print 'show products post'
		form = self.form(request.POST)
		print 'show products form = self.form'
		print form.errors
		if form.is_valid():
			print 'form validated'
			print form.errors
			form.save()
			print 'form saved'
			print form.errors
			return render(request, 'login/shop.html')
		else:
			print form.errors
			context = {'form':form}
			print 'error with save'
			return render(request, 'login/add_product.html', context)