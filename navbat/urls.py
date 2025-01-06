# navbat/urls.py
from django.contrib import admin
from django.urls import path, include
from registration import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Bosh sahifa
    path('register/', views.register, name='register'),  # Navbat qo'shish
]
