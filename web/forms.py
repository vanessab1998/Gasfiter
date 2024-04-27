from django import forms
from .models import Contacto

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['full_name', 'email_contact','subject_contact','phone_number','message_contact']