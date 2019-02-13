from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Student


class UserCreationForm(UserCreationForm):
    regno = forms.IntegerField(required=True)

    class Meta:
        model = User
        fields = ('regno', 'username', 'email', 'password1', 'password2')
        help_texts = {
            'username': '',
            'email': '',
            'password1': '',
            'password2': '',
        }

    def clean_regno(self):
        adlist = Student.objects.all().values_list('reg_no')
        a = self.cleaned_data.get('regno')
        if a in adlist:
            raise forms.ValidationError('ERROR')
