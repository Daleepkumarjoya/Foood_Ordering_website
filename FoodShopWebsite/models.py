from django.db import models
from autoslug import AutoSlugField

# Create your models here.
from django.utils.timezone import now


class HomeModel(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    Desc = models.TextField()
    image = models.ImageField(upload_to='images')
    Home_slug = AutoSlugField(populate_from='name', unique=True, null=True, default=None)

    def __str__(self):
        return self.name


class AboutModel(models.Model):
    image = models.ImageField(upload_to='images')
    Desc = models.TextField()
    delivery = models.CharField(max_length=300)
    payment = models.CharField(max_length=300)
    service = models.CharField(max_length=300)


class MenuModel(models.Model):
    image = models.ImageField(upload_to='images')
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    Desc = models.TextField()
    menu_slug = AutoSlugField(populate_from='name', unique=True, null=True, default=None)

    def __str__(self):
        return self.name


class contacModel(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField(default=0)
    address = models.TextField()
    Query = models.TextField()

    def __str__(self):
        return self.name


class OrderModel(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField(default=0)
    foodName = models.CharField(max_length=200)
    AdditionalFood = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    myDate = models.DateTimeField(auto_now=now)
    address = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name