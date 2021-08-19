from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def home(request):
    return render(request, 'home.html')


def about_owner(request):
    return render(request, 'about_owner.html')


def wines(request):
    return render(request, 'wines.html')


def dining(request):
    return render(request, 'dining.html')


def lodges(request):
    return render(request, 'lodges.html')


def packages(request):
    return render(request, 'packages.html')


def events(request):
    return render(request, 'events.html')


def seasonal(request):
    return render(request, 'seasonal.html')


def special_offers(request):
    return render(request, 'special_offers.html')


def recreation(request):
    return render(request, 'recreation.html')


def travel(request):
    return render(request, 'travel.html')


def customer_stories(request):
    return render(request, 'customer_stories.html')


def privacy(request):
    return render(request, 'privacy.html')


def legal(request):
    return render(request, 'legal.html')


def contact(request):
    return render(request, 'contact.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=request.POST['username'], password=request.POST['password1'])
            
            if user:
                messages.info(request, 'Thank you, for signing up!')
                login(request, user)

                messages.info(request, 'Account created successfully!')
                return redirect('rates')

            else:
                messages.add_message(request, messages.ERROR, 'Unable to log in new user')
        else:
            messages.add_message(request, messages.INFO, 'Please check the data you entered')
            # include the invalid form, which will have error messages added to it. The error messages will be displayed by the template.
            return render(request, 'register.html', {'form': form} )

    form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form} )