from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from haystack.forms import SearchForm, ModelSearchForm
from haystack.generic_views import SearchView
from .models import Example
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
    form = TopicForm()
    return render(request, 'ask.html', {"form": form})
