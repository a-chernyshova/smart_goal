# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from mainapp.models import Tasks


class MyRegistrationForm(UserCreationForm):
    username = forms.CharField(label='User name', widget=forms.TextInput(attrs={'placeholder':'User name'}))
    password2 = forms.CharField(label='Repeat the password', required=False, help_text='Repeat the password correctly')
    email = forms.EmailField(required=True, error_messages='')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')

class TasksForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ('__all__')