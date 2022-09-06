from socket import fromshare
from django import forms

class first_form(forms.Form):
    email = forms.EmailField(),
    password = forms.PasswordInput(),
    addres = forms.CharField(widget=forms.Textarea),
    city = forms.CharField(),
    state = forms.CharField(),
    zip = forms.DecimalField(),
    