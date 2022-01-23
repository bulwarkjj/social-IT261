from django import forms 

class LoginForm(forms.Form):
    """
    Login form to authenticate users against database
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)