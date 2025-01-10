from django.contrib import admin
from .models import Registration , Announcement, Card

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    # Admin panelda ko'rsatiladigan ustunlar
    list_display = ('id', 'Ism_Familyangiz', 'Telefon_raqamingiz', 'Manzil', 'Navbatga_yozilgan_vaqt')
    # Filtrlash uchun maydonlar
    list_filter = ('Manzil', 'Navbatga_yozilgan_vaqt')
    # Qidiruv uchun maydonlar
    search_fields = ('Ism_Familyangiz', 'Telefon_raqamingiz', 'Navbat_olishning_sababi')
    # Ro'yxatni standart tartibda ko'rsatish
    ordering = ('Navbatga_yozilgan_vaqt',)
@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at', 'image')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'content')

class CardAdmin(admin.ModelAdmin):
        list_display = ('title', 'image', 'video_url')
        search_fields = ('title',)

admin.site.register(Card, CardAdmin)