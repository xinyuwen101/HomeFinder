from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from .choices import beds_min_choices, beds_max_choices, price_min_choices, price_max_choices, states_choices
from .forms import ListingForm
from .models import Listing


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }

    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)


def search(request):
    listings = None

    if request.GET:
        listings = Listing.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            listings = listings.filter(
                Q(address__icontains=keywords) | Q(city__icontains=keywords) | Q(state__icontains=keywords) | Q(
                    zipcode__icontains=keywords) | Q(description__icontains=keywords) | Q(address2__icontains=keywords)|Q(title__icontains=keywords))

    # Beds Min
    if 'beds_min' in request.GET:
        beds_min = request.GET['beds_min']
        if beds_min:
            listings = listings.filter(bedrooms__gte=beds_min)

    # Beds Max
    if 'beds_max' in request.GET:
        beds_max = request.GET['beds_max']
        if beds_max:
            listings = listings.filter(bedrooms__lte=beds_max)

    # Beds Min
    if 'price_min' in request.GET:
        price_min = request.GET['price_min']
        if price_min:
            listings = listings.filter(price__gte=price_min)

    # Beds Max
    if 'price_max' in request.GET:
        price_max = request.GET['price_max']
        if price_max:
            listings = listings.filter(price__lte=price_max)

    context = {
        'beds_min_choices': beds_min_choices,
        'beds_max_choices': beds_max_choices,
        'price_min_choices': price_min_choices,
        'price_max_choices': price_max_choices,
        'listings': listings,
        'values': request.GET,
    }

    return render(request, 'listings/search.html', context)


@login_required
def upload(request):
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            new_listing = form.save(commit=False)
            new_listing.user = request.user
            new_listing.save()
            messages.success(request, 'Uploaded successfully')
            return redirect('listings')
        else:
            messages.error(request, 'Information not valid')
            return redirect('upload')
    context = {
        'state_choices': states_choices,
    }
    return render(request, 'listings/upload.html', context)
