from django.shortcuts import render
from products.models import Products


# Create your views here.
def homepage(request):
    popular = Products.objects.all().order_by('-popularity')[:6]
    new_arrival = Products.objects.all().order_by('-date')[:3]

    return render(request, "homepage/homepage.html", {'popular': popular, "new_arrival": new_arrival})


def about(request):
    return render(request, 'homepage/about.html', {})
