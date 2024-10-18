from django.urls import path, include
from django.contrib import admin
from app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('personel/', include('personel.urls')),
    path('admin/', admin.site.urls),
]
