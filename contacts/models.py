from datetime import datetime

from django.db import models


class Contact(models.Model):
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    message = models.TextField()
    contact_date = models.DateTimeField(default=datetime.now)
    user_id = models.IntegerField()

    class Meta:
        ordering = ('-contact_date',)

    def __str__(self):
        return self.name
