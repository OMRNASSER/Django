
from urllib import request
import uuid
from django.shortcuts import render
from django.http import HttpResponse

from bestproduct.models import Products
from .models import Products 
from .models import Category
from .models import Customer
from .models import  SubCategory ,Cart
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

def cart(request , proid):
  
    return render(request, "pages/cart.html" ,{'pro':Products.objects.get(id = proid)} )


# @login_required(login_url='/login/')
def addcart(request,proid):
    quantity=int(Cart.objects.filter(productid=proid).count())
    if quantity >= 1:
        ca=Cart.objects.get(productid=proid)
        Cart.objects.filter(productid=proid).update(num=int(ca.num)+1)
    else:
        id = request.user.id
        carts=Cart(productid=proid,user_id=id,num=1)
        carts.save()
    return redirect("/cartitem/")

#@login_required(login_url='/account/login.html/')
def deleteitem(request,proid):
    item=Cart.objects.get(id=proid)
    item.delete()
    return redirect("/cartitem/")

#@login_required(login_url='/login/')
def cartitem(request):
    quantity = 0
    price =0
    products = product.objects.all()
    orderss = Cart.objects.filter(user_id=request.user.id)
    for v in orderss:
        quantity=quantity+int(v.num)
        for f in product.objects.all():
            if v.productid ==f.id:
                price =price +(int(f.price)*int(v.num))
    return render(request, 'pages/cartitem.html',{"products":products,'quantity':quantity,"price":price,"orders":cart})