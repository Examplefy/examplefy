from django import forms
from django.core import urlresolvers
from django.db import models
from examplefy.models import Example, Topic
from haystack.forms import SearchForm
import widgets

class AskForm(forms.ModelForm):

    def is_valid(self): return True

    class Meta:
        model = Example
        fields = [
            'title',
            'topic',
            'concept',
            'email',
            'content',
            ]

        topic_widget = widgets.ExamplfySelect(model="topic", placeholder="Choose a Topic", attrs={
            'type': 'button',
            'class': 'btn btn-primary dropdown-toggle',
            'data-toggle': 'dropdown',
        })

        concept_widget = widgets.ExamplfySelect(model="concept", placeholder="Choose a Concept", attrs={
            'type': 'button',
            'class': 'btn btn-primary dropdown-toggle',
            'data-toggle': 'dropdown',
        })

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Question Title',
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email Address',
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '10',
            }),
            'topic': topic_widget,
            'concept': concept_widget,
        }
