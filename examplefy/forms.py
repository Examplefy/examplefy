from django.forms import ModelForm, ValidationError
from django import forms
from django.core import urlresolvers
from django.db import models
from examplefy.models import Example, Topic
from haystack.forms import SearchForm

class ExamplfySearchForm(SearchForm):
    topic = forms.ChoiceField()
