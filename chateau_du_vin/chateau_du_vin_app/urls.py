from django.contrib.auth import views as auth_views
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about_owner, name='about'),
    path('wines', views.wines, name='wines'),
    path('dining', views.dining, name='dining'),
    path('lodges', views.lodges, name='lodges'),
    path('packages', views.packages, name='packages'),
    path('events', views.events, name='events'),
    path('seasonal', views.seasonal, name='seasonal'),
    path('special_offers', views.special_offers, name='special_offers'),
    path('recreation', views.recreation, name='recreation'),
    path('travel', views.travel, name='travel'),
    path('customer_stories', views.customer_stories, name='customer_stories'),
    path('privacy', views.privacy, name='privacy'),
    path('legal', views.legal, name='legal'),
    path('contact', views.contact, name='contact'),
    path('register', views.register, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]