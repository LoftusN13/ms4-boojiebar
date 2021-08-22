from django.shortcuts import (
    render, redirect, reverse, HttpResponse)


# Create your views here.
def view_bag(request):
    # view to return shopping bag page
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    # add quantity of specified product into bag

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)


def edit_bag(request, item_id):
    # edit quantity of specified product in bag

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity

    else:
        bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def delete_from_bag(request, item_id):
    # delete specified product from bag

    try:
        bag = request.session.get('bag', {})

        if item_id in bag:
            bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
