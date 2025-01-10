# navbat/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from registration import views
from django.contrib.auth.views import LogoutView
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),  # Admin yo'nalishi
    path('', views.home, name='home'),  # Bosh sahifa
    path('register/', views.register, name='register'),  # To'g'ri nom bering
    path('register_accaunt/', views.register_accaunt, name='register_accaunt'),  # Navbat qo'shish
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


