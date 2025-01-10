# registration/forms.py
from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):

    class Meta:
        model = Registration
        fields = ['Ism_Familyangiz', 'Telefon_raqamingiz', 'Navbat_olishning_sababi', 'Manzil',]
