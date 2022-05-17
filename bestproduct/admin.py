from django.contrib import admin
from .models import Products
from .models import Customer
from .models import Category
from .models import SubCategory , Cart
# Register your models here.
admin.site.register(Products)
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Cart)