from django.db import models
from django.contrib.auth.models import User


User._meta.get_field('email')._unique = True


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    firstName = models.CharField(max_length=100, blank=False)
    lastName = models.CharField(max_length=100, blank=False)
    phone = models.PositiveIntegerField(null=False, blank=False)
    email = models.CharField(null=False, blank=False, max_length=100)
    balance = models.DecimalField(null=True, decimal_places=2, max_digits=10)
    guest = models.BooleanField(null=False)


class Wine(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100)
    year = models.PositiveIntegerField(null=False, blank=False)
    origin = models.CharField(null=False, blank=False, max_length=200)
    price = models.DecimalField(null=False, blank=False, decimal_places=2, max_digits=10)
    inStock = models.BooleanField(null=False, blank=False)
    quantity = models.PositiveIntegerField(null=False, blank=False)
    bottleSize = models.DecimalField(null=False, blank=False, decimal_places=1, max_digits=10)


class Food(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100)
    category = models.CharField(null=False, blank=False, max_length=100)
    price = models.DecimalField(null=False, blank=False, decimal_places=2, max_digits=10)
    available = models.BooleanField(null=False, blank=False)


class Lodge(models.Model):
    lodgeNumber = models.PositiveIntegerField(null=False, blank=False)
    squareFeet = models.PositiveIntegerField(null=False, blank=False)
    numBedrooms = models.PositiveIntegerField(null=False, blank=False)
    numBathrooms = models.PositiveIntegerField(null=False, blank=False)
    operational = models.BooleanField(null=False, blank=False)
    available = models.BooleanField(null=False, blank=False)
    view = models.CharField(null=False, blank=False, max_length=100)
    pricePerNight = models.DecimalField(null=False, blank=False, decimal_places=2, max_digits=10)
    pricePerWeek = models.DecimalField(null=False, blank=False, decimal_places=2, max_digits=10)


class Reservation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    lodge = models.ForeignKey(Lodge, on_delete=models.SET_NULL, null=True)
    dayOnly = models.BooleanField(null=False, blank=False)
    numNights = models.PositiveIntegerField(null=True, blank=False)
    totalCost = models.DecimalField(null=False, blank=False, decimal_places=2, max_digits=10)
