from django import forms
from .models import Profile


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'address', 'postcode', 'contact']
