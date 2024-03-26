from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages


# Create your views here.

from django.shortcuts import render

from bookstore.settings import BASE_DIR
from .models import Book
from .models import ContactMessage

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

# def index(request):
#     return render(request, 'index.html')
def navbar(request):
  return render(request, 'book_list.html')

def about(request):
    return render(request, 'books/about.html')

def contact(request):
    return render(request, 'books/contact.html')


def submit_contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        ContactMessage.objects.create(name=name, email=email, message=message)

        messages.success(request, f'Thank you, {name}, for your submission!')

        return redirect('contact')
    else:
        return redirect('contact')
