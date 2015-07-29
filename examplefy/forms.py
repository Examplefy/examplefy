from django.forms import ModelForm, ValidationError
from django import forms
from django.core import urlresolvers
from django.db import models
from examplefy.models import Example, Topic

class TopicForm(forms.Form):
    """
    A form used to ask a what topic a question will be
    """
    topic = forms.ModelChoiceField(queryset=Topic.objects.all(), empty_label="(Nothing)")
