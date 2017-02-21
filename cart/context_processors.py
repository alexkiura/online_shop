"""Context processors for cart."""
from cart.helper import Cart


def cart(request):
    return {'cart': Cart(request)}
