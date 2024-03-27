from django import template
from books.models import Cart, CartItem

register = template.Library()

@register.simple_tag(takes_context=True)
def get_cart_item_count(context):
    request = context['request']
    total_items = 0
    cart_id = request.session.get('cart_id')
    if cart_id:
        try:
            cart = Cart.objects.get(id=cart_id)
            total_items = sum(item.quantity for item in CartItem.objects.filter(cart=cart))
        except Cart.DoesNotExist:
            pass
    return total_items