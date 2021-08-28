from django.shortcuts import render

# Create your views here.


def profile(request):
    # Displays user's profile

    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
