from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    email = forms.EmailField(label="email",widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'firstname'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'lastname'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'username'}))
    password1 = forms.CharField(label="password",widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}))
    password2 = forms.CharField(label="password conformation",widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'re-enter password'}))

    class Meta:
        model = User
        fields =[
             'first_name','last_name','username','password1','password2','email'
        ]


class DepartmentRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}))
    email = forms.EmailField(label="email",widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}))
    password1 = forms.CharField(label="password",widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))
    password2 = forms.CharField(label="password conformation", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 're-enter password'}))

    class Meta:
        model = User
        fields = [
             'username','email','password1','password2']