from django.urls import path
from . import views
from django.shortcuts import render
from .models import ContactMessage
from .views import LogoutWithGet, clear_cart, UserLoginView 
from django.contrib.auth.views import LoginView
from .views import logout_view




urlpatterns = [
   path("", views.book_list, name='book_list'),
   path("about/", views.about, name="about"), 
   path("contact/", views.contact, name="contact"),
   path("navbar", views.navbar, name='navbar'),
   path('submit-contact-form', views.submit_contact_form, name='submit_contact_form'),
   path('cart/', views.cart_detail, name='cart_detail'),
   path('add_to_cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
   path('clear-cart/', clear_cart, name='clear_cart'),
   path('logout/', logout_view, name='logout'),
   path('login/', LoginView.as_view(template_name='books/login.html'), name='login'),





]

