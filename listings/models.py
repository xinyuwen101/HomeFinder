from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Listing(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    address2 = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(default=0)
    bedrooms = models.IntegerField(default=0)
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    sqft = models.IntegerField(default=0)
    type = models.CharField(max_length=20, null=True, blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, blank=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        ordering = ('-list_date',)

    def __str__(self):
        return self.title
