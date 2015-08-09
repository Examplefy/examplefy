from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from haystack.forms import SearchForm, ModelSearchForm
from haystack.generic_views import SearchView
from .models import Example, Topic, Concept
from .forms import *

def homepage(request):
    if request.method == "POST":
        form = SearchFrom(request.form)
        if form.is_valid():
            return HttpResposeRedirect("/")
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
    data_for_form = {}
    data_for_form["topics"] = Topic.objects.all()

    return render(request, 'ask.html', {"data": data_for_form})

    """
    form = TopicForm()
    entered_data = {}
    entered_data["topics"] = Topic.objects.all()
    if not "topic" in request.GET:
        entered_data["state"] = "topic"
    elif not "concepts" in request.GET:
        entered_data["topic"] = request.GET['topic']
        entered_data["state"] = "concept"
        print Concept.objects.all().filter(topic=Topic(name=entered_data["topic"]))
        entered_data["concepts"] = Concept.objects.all().filter(topic=Topic(name=entered_data["topic"]))
    return render(request, 'ask.html', {"form": form, "entered_data": entered_data})
    """
