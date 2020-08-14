from django.shortcuts import render
from .models import Products

# Create your views here.
categories = ["AGRICULTURE POWER SPRAYER", "AIR & VACUUM PUMP", "CAR WASHERS",
              "COMPRESSOR", "ELECTRIC MOTORS", "FOAM GUN",
              "FOAM TANK", "GARAGE EQUIPMENT & ACCESSORIES",
              "GREASE PUMP", "HI-PRESSURE PUMP & PIPE",
              "IMPACT WRENCH", "PNEUMATIC FITTING",
              "SPRAY GUN", "TIRE INFLATING GUN",
              "VACUUM CLEANERS", "WELDING MACHINE",
              "AGRICULTURE SPRAYER PARTS", "HARDWARE ITEMS"]


def products(request):
    products_relevance = Products.objects.all().order_by('rank')
    products_h_price = Products.objects.all().order_by('price')[::-1]
    products_l_price = Products.objects.all().order_by('price')

    return render(request, 'products/products.html',
                  {"l_price": products_l_price, 'h_price': products_h_price, 'products_relevance': products_relevance,
                   'categories': categories})


def categories_product(request, category):
    cat = category[1:-1]
    products_relevance = Products.objects.filter(Category=cat).order_by('rank')
    products_h_price = Products.objects.filter(Category=cat).order_by('price')[::-1]
    products_l_price = Products.objects.filter(Category=cat).order_by('price')

    return render(request, 'products/cat.html',
                  {"l_price": products_l_price, 'h_price': products_h_price, 'products_relevance': products_relevance,
                   'categories': categories, 'cat': cat})
