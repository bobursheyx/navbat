# registration/views.py
from django.shortcuts import render, redirect
from .models import Registration
from .forms import RegistrationForm

def home(request):
    # Mavjud navbatlarni olish
    navbatlar = Registration.objects.all()
    return render(request, 'registration/home.html', {'navbatlar': navbatlar})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Bosh sahifaga qaytish
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
