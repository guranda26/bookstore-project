from django.urls import path
from . import views
from django.shortcuts import render
from .models import ContactMessage

urlpatterns = [
   path("", views.book_list, name='book_list'),
   path("about/", views.about, name="about"), 
   path("contact/", views.contact, name="contact"),
   path("navbar", views.navbar, name='navbar'),
   path('submit-contact-form', views.submit_contact_form, name='submit_contact_form'),
   
]

