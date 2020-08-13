from django.shortcuts import render
from .models import Products
# Create your views here.

def products(request):
    return render(request, 'timezone/shop.html', {})