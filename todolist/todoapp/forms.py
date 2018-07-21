from django import forms
from todoapp.models import *


class Addlist(forms.ModelForm):
    class Meta:
        model = Todo_info
        exclude = ['id']
        widgets = {
            'task_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'task_info': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter taskinfo'}),
            'actual_date': forms.DateTimeInput(format='%Y-%m-%d %H:%M:%S',
                                               attrs={'class': 'form-control', 'placeholder': 'Enter date and time'}),
            'status': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter status'}),
        }


class Signupform(forms.Form):
    first_name = forms.CharField(
        max_length=75,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Firstname'})
    )
    last_name = forms.CharField(
        max_length=75,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Lastname'})
    )
    username = forms.CharField(
        max_length=75,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'})
    )
    password = forms.CharField(
        max_length=75,
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'})
    )


class Loginform(forms.Form):
    username = forms.CharField(
        max_length=75,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'})
    )
    password = forms.CharField(
        max_length=75,
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'})
    )
