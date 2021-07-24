from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def home(request):
    return render(request, 'home.html')


def rates(request):
    return render(request, 'rates.html')

def about_owner(request):
    return render(request, 'about_owner.html')


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