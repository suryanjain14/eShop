from django.contrib import admin
from django.urls import path
from homepage import views as hv
from products import views as pv
from contactus import views as cv
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hv.homepage, name='home'),
    path('home/', hv.homepage, name='home'),
    path('shop/', pv.products, name='product'),
    path('<category>', pv.categories_product, name='product_category'),
    path('about/', hv.about, name='about'),
    path('contact/', cv.contact, name='contact'),
    path('product/<pk>', pv.product_detail, name='product_details')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
