from django.contrib import admin
from django.urls import path
from homepage import views as hv
from products import views as pv
from contactus import views as cv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hv.homepage, name='home'),
    path('home/', hv.homepage, name='home'),
    path('shop/', pv.products, name='product'),
    path('about/', hv.about, name='about'),
    path('contact/', cv.contact, name='contact')
]
