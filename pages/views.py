from django.shortcuts import render

from listings.choices import price_choices, bedroom_choices, state_choices
from listings.models import Listing


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }

    return render(request,
                  'pages/index.html',
                  context)
