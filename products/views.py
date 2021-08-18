from django.shortcuts import render, get_object_or_404
from .models import Product


# Create your views here.
def all_products(request):
    # view to return all products page
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_details(request, product_id):
    # view to return details of each individual product
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_details.html', context)
