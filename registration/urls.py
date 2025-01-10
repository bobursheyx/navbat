from django.urls import path
from . import views
from .views import update_registration, delete_registration

app_name = 'registered'
urlpatterns = [
    path('update/<int:id>/',update_registration , name='update_registration'),
    path('delete/<int:id>/', delete_registration, name='delete_registration'),
    # Boshqa yo'nalishlar...
    path('', views.home, name='home'),  # Home sahifa
]
