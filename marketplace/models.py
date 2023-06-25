from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class AccReg(AbstractUser):
    is_buyer = models.BooleanField(default=False)
    email = models.EmailField()
    name = models.CharField(max_length=20, null=True)
    mobile = models.CharField(max_length=20, null=True , unique=True)
    address = models.CharField(max_length=100, null=True)
    username = models.CharField(max_length=30,unique=True)

    def __str__(self):
        return str(self.name)

class AddProduct(models.Model):
    Type = [
        ('fs', 'Fashion'),
        ('ec', 'Electronics'),
        ('gc', 'Grocery')
    ]
    product_name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    image = models.ImageField(upload_to='products',default='blank_pro_pic.jpg')
    category = models.CharField(max_length=20, choices=Type)
    brand = models.CharField(max_length=20)
    created_date = models.DateTimeField(default=datetime.now)
    last_update = models.DateTimeField(default=datetime.now)

class Cart(models.Model):
    user = models.ForeignKey(AccReg, on_delete=models.CASCADE)
    products = models.ManyToManyField(AddProduct)


