from django.contrib.auth.forms import AuthenticationForm, UsernameField

from django import forms


class UserForm(forms.Form):

    # # username = forms.CharField(widget=forms.TextInput(attrs={'name':"username", 'class':'input100'}))
    # passw= forms.PasswordInput(attrs={'name':"passw", 'class':'input100', 'type':'password'})
    passn=forms.CharField(widget=forms.PasswordInput(attrs={'name':"passn", 'class':'input100', 'type':'password', 'minlength':6}))
    passnc=forms.CharField(widget=forms.PasswordInput(attrs={'name':"passnc", 'class':'input100', 'type':'password', 'minlength':6}))


class LoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={'name':"username", 'class':'input100'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'name':"password", 'class':'input100', 'type':'password'}))
