from django.contrib.auth import get_user_model
from django import forms

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['password']