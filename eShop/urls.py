
from django.contrib import admin
from django.urls import path
from homepage import views as hv
from products import  views as pv


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hv.h, name='home'),
    path('shop/', pv.products, name='product'),
    path('about/', hv.about, name='about')
]
