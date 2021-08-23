from django.shortcuts import (
    render, redirect, reverse, HttpResponse,
    get_object_or_404)
from django.contrib import messages
from products.models import Product


# Create your views here.
def view_bag(request):
    # view to return shopping bag page
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    # add quantity of specified product into bag

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(
            request, f'Updated {product.name} quantity to {bag[item_id]}!')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag!')

    request.session['bag'] = bag
    return redirect(redirect_url)


def edit_bag(request, item_id):
    # edit quantity of specified product in bag

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request, f'Updated {product.name} quantity to {bag[item_id]}!')

    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag!')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def delete_from_bag(request, item_id):
    # delete specified product from bag

    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})

        if item_id in bag:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag!')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
