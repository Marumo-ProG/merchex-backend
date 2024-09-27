from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

current_year = datetime.date.today().year


# Create your models here.
class Band(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    year_formed = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1900),  # Replace with a reasonable minimum year
            MaxValueValidator(current_year),
        ]
    )
    genre = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="bands/", null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    band = models.ForeignKey(Band, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Listing(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to="listings/", null=True, blank=True)
    is_active = models.BooleanField(default=True)
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
