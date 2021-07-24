from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


def rates(request):
    return render(request, 'rates.html')

def about_owner(request):
    return render(request, 'about_owner.html')