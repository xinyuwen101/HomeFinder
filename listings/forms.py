from django import forms

from .models import Listing


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = (
            'title', 'address', 'address2', 'city', 'state', 'zipcode', 'description', 'price', 'bedrooms', 'bathrooms',
            'sqft', 'photo_main', 'photo_1', 'photo_2', 'photo_3', 'photo_4', 'photo_5', 'deposit'
        )
