
from django.contrib import admin
from django.urls import path
from homepage import views as hv
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hv.h, name='home'),
]
