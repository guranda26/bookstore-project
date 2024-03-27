from django.contrib import admin

# Register your models here.

from .models import Book, ContactMessage, CartItem
from django.contrib import admin


admin.site.register(Book)

admin.site.register(ContactMessage)

admin.site.register(CartItem)



