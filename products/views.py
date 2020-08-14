from django.shortcuts import render
from .models import Products


# Create your views here.

def products(request):
    products_relevance = Products.objects.all().order_by('rank')
    products_h_price = Products.objects.all().order_by('price')[::-1]
    products_l_price = Products.objects.all().order_by('price', )

    return render(request, 'products/products.html',
                  {"l_price": products_l_price, 'h_price': products_h_price, 'products_relevance': products_relevance})
