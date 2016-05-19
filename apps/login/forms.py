from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Product, Order
from django.forms import ModelForm
from django.utils import timezone

class User_form(UserCreationForm):
    username = forms.CharField(label='User name', max_length=200)
    first_name = forms.CharField(label='First Name', max_length=200)
    last_name = forms.CharField(label='Last Name', max_length=200)
    email = forms.EmailField(label='Email', max_length=200)
    
    class Meta:
        model = User
        # fields = "__all__"
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    
    def save(self, commit=True):
        user = super(User_form, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
            return user


class Auth_form(forms.Form):
    username = forms.CharField(label='User name', widget=forms.TextInput)
    password = forms.CharField(label='Pwd', widget=forms.PasswordInput)

    class Meta:
        fields = ('username', 'password')


class Product_form(ModelForm):
    
    class Meta:
        model = Product
        fields = ('product_name', 'description', 'price', 'image_url', 'quantity')
    
    def save(self, commit=True):
        product = super(Product_form, self).save(commit=False)
        product.product_name = self.cleaned_data['product_name']
        product.description = self.cleaned_data['description']
        product.price = self.cleaned_data['price']
        product.image_url = self.cleaned_data['image_url']
        product.quantity = self.cleaned_data['quantity']
        if commit:
            product.save()
            return product


class Order_form(ModelForm):
    product = forms.CharField(widget=forms.HiddenInput())
    user = forms.CharField(widget=forms.HiddenInput())
    credit_card = forms.IntegerField()
    cid_num = forms.IntegerField()
    cc_exp_date = forms.DateField()

    class Meta:
        model = Order
        fields = ('product', 'user','credit_card', 'cid_num', 'cc_exp_date')

    def save(self, commit=True):
        order = super(Order_form, self).save(commit=False)
        order.credit_card = self.cleaned_data['credit_card']
        order.cid_num = self.cleaned_data['cid_num']
        order.cc_exp_date = self.cleaned_data['cc_exp_date']
        order.product = self.cleaned_data['product']
        order.user = self.cleaned_data['user']
        print 'order_form save'
        if commit:
            print 'before save'
            order.save()
            print 'after save'
            return order