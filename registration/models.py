# registration/models.py
from django.db import models
from django.contrib.auth.models import User

class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Foydalanuvchi bilan bog'lash
    LOCATION_A = '🏥 Манзил: Маргилон шахар'
    LOCATION_B = '🏥 Манзил: Сой буйи Дилобар медикал'
    LOCATION_CHOICES = [
        (LOCATION_A, '🏥 Манзил: Маргилон шахар (комбинат ) 6-поликлиника 61-хона 3-кават🕛 кабул вакти 14:00дан 17:00гача.'),
        (LOCATION_B, '🏥 Манзил: Сой буйи Дилобар медикал (шахар болалар шифохонаси ёнида)🕛 кабул вакти 18:30 дан 20: 30 гача.'),
    ]
    Ism_Familyangiz = models.CharField(max_length=100)
    Telefon_raqamingiz = models.IntegerField()
    Navbat_olishning_sababi = models.TextField()
    Manzil = models.CharField(
        max_length=2000,
        choices=LOCATION_CHOICES,
        verbose_name="Manzilni tanlang",
        default=LOCATION_A  # Standart tanlov
    )
    Navbatga_yozilgan_vaqt = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    def __str__(self):
        return f"{self.Ism_Familyangiz} ({self.user.username})"

class Announcement(models.Model):
    title = models.CharField(max_length=255)  # E'lon sarlavhasi
    content = models.TextField()  # E'lon mazmuni
    is_active = models.BooleanField(default=True)  # Faol yoki yo'qligini aniqlash
    image = models.ImageField(upload_to='announcements/', blank=True, null=True)  # Rasm maydoni
    created_at = models.DateTimeField(auto_now_add=True)  # Qo'shilgan vaqt

    def __str__(self):
        return self.title


class Card(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='card_images/')
    video_url = models.URLField()

    def __str__(self):
        return self.title