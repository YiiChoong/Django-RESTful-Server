from django.db import models

# Create your models here.

class Car(models.Model):
    make = models.CharField(max_length=60)
    model = models.CharField(max_length=60)
    year = models.PositiveSmallIntegerField()
    seats = models.PositiveSmallIntegerField()
    color = models.CharField(max_length=60)
    vin = models.CharField(max_length=17)
    current_mileage = models.PositiveIntegerField(help_text="miles")
    service_interval = models.PositiveIntegerField(help_text="miles")
    next_service = models.PositiveIntegerField(help_text="miles")

class Truck(models.Model):
    make = models.CharField(max_length=60)
    model = models.CharField(max_length=60)
    year = models.PositiveSmallIntegerField()
    seats = models.PositiveSmallIntegerField()
    bed_length = models.PositiveIntegerField(help_text="inches")
    color = models.CharField(max_length=60)
    vin = models.CharField(max_length=17)
    current_mileage = models.PositiveIntegerField(help_text="miles")
    service_interval = models.PositiveIntegerField(help_text="miles")
    next_service = models.PositiveIntegerField(help_text="miles")

class Boat(models.Model):
    make = models.CharField(max_length=60)
    model = models.CharField(max_length=60)
    year = models.PositiveSmallIntegerField()
    length = models.PositiveIntegerField(help_text="feet")
    width = models.PositiveIntegerField(help_text="inches")
    hin = models.CharField(max_length=17)
    current_hours = models.PositiveSmallIntegerField(help_text="hours")
    service_interval = models.PositiveIntegerField(help_text="miles")
    next_service = models.PositiveIntegerField(help_text="miles")
