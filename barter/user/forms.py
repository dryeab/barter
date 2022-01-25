from django import forms

from .models import User


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "fullname", "email", "phone", "password"]


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["fullname", "phone", "profile_picture", "bio"]
