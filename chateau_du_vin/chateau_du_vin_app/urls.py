from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('rates', views.rates, name='rates'),
    path('about', views.about_owner, name='about')
]