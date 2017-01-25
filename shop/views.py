"""Application views."""

from django.shortcuts import get_object_or_404, render
from shop.models import Category, Product


def product_list(request, category_slug=None):
    """Render a list of products in the store."""
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, product_id, slug):
    """Render a single product."""
    product = get_object_or_404(Product,
                                id=product_id,
                                slug=slug,
                                available=True)
    return render(request,
                  'shop/product/detaul.html',
                  {'product': product})
