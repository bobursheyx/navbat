from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Bosh sahifa uchun yo'nalish
    path('success/', views.success, name='success'),
]
