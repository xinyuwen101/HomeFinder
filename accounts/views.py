from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.utils.translation import gettext as _

from contacts.models import Contact
from listings.models import Listing


def register(request):
    if request.method == 'POST':
        # Get form values
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, _('That username is taken'))
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, email=email,
                                                first_name=first_name, last_name=last_name)
                # Login after register
                user.save()
                auth.login(request, user)
                messages.success(request, _('You are now logged in'))
                return redirect('index')
                # messages.success(request, 'You are now registered and can log in')
                # return redirect('login')
        else:
            messages.error(request, _('Passwords do not match'))
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, _('You are now logged in'))
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(next)
        else:
            messages.error(request, _('Invalid credentials'))
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, _('You are now logged out'))
        return redirect('index')


@login_required
def dashboard(request):
    listings = Listing.objects.filter(user=request.user)
    contacts = Contact.objects.all()

    context = {
        'contacts': contacts,
        'listings': listings
    }

    return render(request, 'accounts/dashboard.html', context)
