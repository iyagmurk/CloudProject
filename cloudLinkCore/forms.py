# forms.py
from django import forms

class ShortenURLForm(forms.Form):
    long_url = forms.URLField()
