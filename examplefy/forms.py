from django.forms import ModelForm, ValidationError
from django import forms
from django.core import urlresolvers
from django.db import models
from examplefy.models import Tag, Example

# Not using this right now
class SearchForm(forms.Form):
    """
    A form used to search the database for examples
    """
    search_term = forms.CharField(max_length=100)
