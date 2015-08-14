from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from haystack.forms import SearchForm, ModelSearchForm
from haystack.generic_views import SearchView
from .models import Example, Topic, Concept
from .forms import *
import json

def homepage(request):
    if request.method == "POST":
        form = SearchFrom(request.form)
        if form.is_valid():
            return HttpResponseRedirect("/")
    else:
        form = SearchForm()
        return render(request, 'index.html', {"logged_in": request.user.is_authenticated(), "form": form})

def logout_user(request):
    print("hi")
    #logout(request)
    return homepage(request)

def search(request):
    pass

class ExamplefySearchView(SearchView):
    template_name = 'index.html'
    form_class = SearchForm

def ask_view(request):
    data = {}
    data["topics"] = [topic.name for topic in list(Topic.objects.all())]
    data["concepts"] = {}
    for topic in data["topics"]:
        data["concepts"][topic] = [concept.name for concept in list(Concept.objects.all().filter(topic__name=topic))]
    data["json"] = json.dumps(data)
    return render(request, 'ask.html', {"data": data})

def add_example_view(request):
    title = "placeholder_title"
    topic = Topic.objects.get(name=request.POST['topic'])
    concept = Concept.objects.get(name=request.POST['concept'])
    text = request.POST['text']
    Example(title=title, topic=topic, concept=concept, content=text).save()
    return render(request, 'question_asked.html')
