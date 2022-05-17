
from urllib import request
import uuid
from django.shortcuts import render
from django.http import HttpResponse

from bestproduct.models import Products
from .models import Products 
from .models import Category
from .models import Customer
from .models import  SubCategory
# Create your views here.


def products (request):
    return render(request , 'pages/index.html',{'pro':Products.objects.order_by('-id') , 'cat':Category.objects.all() })

def product (request , proid):
    myproduct = Products.objects.get(id = proid)
    return render(request , 'pages/product-details.html' , {'product':myproduct} ) 

def category(request , categoryid):
    mycategory = Category.objects.get(id = categoryid)
    return render(request ,'pages/shop.html',{'pro': Products.objects.order_by('-id').filter(cat = categoryid), 'cat':Category.objects.all().filter(id = categoryid) , 'mycat':mycategory} )


def product_shop (request , proid):
    myproduct = Products.objects.get(id = proid)
    return render(request , 'pages/product-details.html' , {'product':myproduct} ) 

def login(request):
   return render (request , "pages/login.html" )

def cart(request):
  
    return render(request, "pages/cart.html" )