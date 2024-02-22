from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(forms.Form):
    user_name = forms.CharField(max_length=50, widget=forms.TextInput())
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    password_1 = forms.CharField(max_length=50, widget=forms.PasswordInput())
    password_2 = forms.CharField(max_length=50, widget=forms.PasswordInput())

    def clean_user_name(self):
        user = self.cleaned_data["user_name"]
        if User.objects.filter(username=user).exists():
            raise forms.ValidationError("This user exist!")
        return user

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email exist!")
        return email

    def clean_password_2(self):
        password_2 = self.cleaned_data["password_2"]
        password_1 = self.cleaned_data["password_1"]
        if password_2 != password_1:
            raise forms.ValidationError("passwords are not the same!")
        return password_1


class UserLoginForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Email or username"})
    )
    password = forms.CharField(max_length=50, widget=forms.PasswordInput())
