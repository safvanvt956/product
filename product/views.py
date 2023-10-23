from django.shortcuts import render
from django.views.generic import ListView
from .models import Product,Category,Subcategory

# Create your views here

class Productview(ListView):
    model = Product
    template_name = "index.html"
    context_object_name = 'products'


class Product(ListView):
    model = Product
    template_name = "product.html"
    context_object_name = 'products'


class CategoryView(ListView):
    model = Category
    template_name = "category.html"
    context_object_name = 'categorys'


class Subcategory(ListView):
    model = Subcategory
    template_name = "subcategory.html"
    context_object_name = 'subcate'





    







