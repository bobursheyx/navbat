from django.contrib.auth import logout
from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Registration, Announcement, Card
from .forms import RegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

@login_required
def home(request):
    # Foydalanuvchining navbatlarini olish
    navbatlar = Registration.objects.filter(user=request.user)
    cards = Card.objects.all()

    # Faol e'lonlarni olish
    announcements = Announcement.objects.filter(is_active=True).order_by('-created_at')[:5]  # Eng oxirgi 5 e'lon

    return render(request, 'registration/home.html', {
        'navbatlar': navbatlar,
        'announcements': announcements,
        'cards': cards
    })

@login_required
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            navbat = form.save(commit=False)
            navbat.user = request.user  # Navbatni foydalanuvchi bilan bog'lash
            navbat.save()
            return redirect('home')  # Bosh sahifaga qaytish
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})




from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register_accaunt(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Foydalanuvchi yaratish
            messages.success(request, 'Akkount yaratildi! Endi tizimga kiring.')  # Xabar yuborish
            return redirect('login')  # Tizimga kirish sahifasiga yo'naltirish
    else:
        form = UserCreationForm()  # Formani yaratish

    return render(request, 'registration/register_accaunt.html', {'form': form})


from django.http import JsonResponse

@login_required
def update_registration(request, id):
    navbat = get_object_or_404(Registration, id=id, user=request.user)
    if request.method == 'POST':
        form = RegistrationForm(request.POST, instance=navbat)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': 'Yangilandi!'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Faqat POST soʻrovi qabul qilinadi!'})

@login_required
def delete_registration(request, id):
    navbat = get_object_or_404(Registration, id=id, user=request.user)
    if request.method == 'POST':
        navbat.delete()
        return JsonResponse({'status': 'success', 'message': 'Oʻchirildi!'})
    return JsonResponse({'status': 'error', 'message': 'Faqat POST soʻrovi qabul qilinadi!'})


# Logout funksiyasi
def logout_view(request):
    logout(request)
    return redirect('login')