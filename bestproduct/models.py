from distutils.command import upload
from tkinter import CASCADE, Image
from django.db import models

# Create your models here.
class Category (models.Model):
    cat_name = models.CharField(max_length=50)
    cat_type = models.CharField(max_length=50)
    def __str__(self):
        return self.cat_name

class Products (models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8 ,decimal_places=2 )
    desc  = models.TextField()
    image =models.ImageField(upload_to ='images/')
    active  = models.BooleanField(default= True)
    review  = models.DecimalField(max_digits=5 , decimal_places=1)
    cat = models.ForeignKey( Category, on_delete = models.CASCADE )
    def __str__(self):
        return self.name


class Customer (models.Model):
    name = models.CharField(max_length=70)
    contact = models.EmailField(max_length=60)
    PhoneNumber =models.CharField(max_length=12)
    address = models.TextField()
    def __str__(self):
            return self.name


class SubCategory (models.Model):
    sub_name = models.CharField(max_length=40)
    cat_id = models.ForeignKey(Category ,default=1 , blank=True , null=True , on_delete=models.CASCADE)
    def __str__(self) :
        return self.sub_name

class Cart(models.Model):
    user = models.ForeignKey(Customer , on_delete = models.CASCADE)
    product_id = models.ForeignKey(Products , on_delete = models.CASCADE)
    qnt = models.IntegerField(null = False  , blank = False)
    created = models.DateTimeField(auto_now_add=True)








