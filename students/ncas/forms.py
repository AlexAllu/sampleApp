from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        help_texts = {
            'username': '',
            'email': '',
            'password1': '',
            'password2': '',
        }



class AdmnoVerification(forms.Form):
    adm_no = forms.IntegerField(required=True)
