"""
Definition of forms.
"""

from django import forms
from app.models import LogMessage

class LogForm(forms.ModelForm):
    class Meta:
        model=LogMessage 
        fields=("title","message","rating")
        

class SearchForm(forms.Form):
    query = forms.CharField(label='Search for a film', max_length=100)
        
     