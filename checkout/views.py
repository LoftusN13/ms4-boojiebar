from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag right now!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JHsV6DCP6ztuKA2bK0gCxz45JRpcawNWnFKZdXWT5GfSROOgW7HXUoSNEpTyn1LvrvxDfxlXSWNjwnc6PhMlDEP00wk6rSIzN',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
