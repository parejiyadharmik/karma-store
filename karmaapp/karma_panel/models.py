from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey
from django.db.models.lookups import IsNull

# Create your models here.
class user(models.Model):
    password=models.CharField(max_length=20)
    otp=models.IntegerField(default=1234)
    firstname=models.CharField(max_length=100)
    contactno=models.BigIntegerField(null=True)
    lastname=models.CharField(max_length=100)
    email=models.EmailField(unique=True,null=True)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    pincode=models.IntegerField(null=True)

class category_dtls(models.Model):
    cid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)

class add_product(models.Model):
    productname=models.CharField(max_length=50,unique=True,null=False)
    productimg=models.ImageField(upload_to='E:/djangoproject/env_swan/karmaapp/media/')
    brand=models.CharField(max_length=50,null=True)
    price=models.IntegerField(null=False)
    # cat_id=models.ForeignKey(category_dtls,on_delete=models.CASCADE)
    Description=models.CharField(max_length=100,null=True)
    
class Cart(models.Model):
    product =models.ForeignKey(add_product, on_delete=models.CASCADE)
    total_quantity= models.CharField(max_length=100, default="quantity")
    price= models.FloatField(max_length=100)
