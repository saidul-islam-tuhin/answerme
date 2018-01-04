from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name', 'email']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo','website','location']


class SignUpFrom(UserCreationForm):
    #photo = forms.ImageField(help_text='Optional',required=False)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )
