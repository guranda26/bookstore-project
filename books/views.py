from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout
from django.shortcuts import redirect
# Create your views here.

from django.shortcuts import render

from bookstore.settings import BASE_DIR
from .models import Book, Cart, CartItem
from .models import ContactMessage

def book_list(request):
    print("User authenticated:", request.user.is_authenticated) 
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})


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




def add_to_cart(request, book_id):
    cart_id = request.session.get('cart_id')
    book = get_object_or_404(Book, id=book_id)

    if cart_id:
        cart = Cart.objects.get(id=cart_id)
    else:
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id
    cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def cart_detail(request):
    cart_id = request.session.get('cart_id', None)
    cart = None
    items = []
    total_items = 0  

    if cart_id:
        try:
            cart = Cart.objects.get(id=cart_id)
            items = CartItem.objects.filter(cart=cart)
            total_items = sum(item.quantity for item in items)  
        except Cart.DoesNotExist:
            pass

    context = {
        'cart': cart,
        'cart_items': items,
        'total_items': total_items,  
    }
    return render(request, 'books/cart_detail.html', context)

def clear_cart(request):
    cart_id = request.session.get('cart_id')
    if cart_id:
        CartItem.objects.filter(cart_id=cart_id).delete()
        del request.session['cart_id']
    return redirect('cart_detail')

def logout_view(request):
    logout(request)
    return redirect('book_list')

class UserLoginView(LoginView):
    template_name = 'books/login.html' 
    redirect_authenticated_user = True
    next_page = reverse_lazy('book_list') 

class LogoutWithGet(LogoutView):
    next_page = reverse_lazy('book_list')

    def get(self, request, *args, **kwargs):
        """Handle logout by a GET request."""
        return self.post(request, *args, **kwargs)

def some_view(request):
    # Accessing the user object
    current_user = request.user
    if current_user.is_authenticated:
        # Now you can access user details
        username = current_user.username
        # Do something with the username or other user details
        ...
    return render(request, 'some_template.html', {})