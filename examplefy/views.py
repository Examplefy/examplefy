from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View, TemplateView
from haystack.forms import SearchForm, ModelSearchForm
from haystack.generic_views import SearchView
from .models import Example, Topic, Concept
from .forms import *
import json



def homepage(request):
    return render(request, 'index.html')

class ExampleSearchView(SearchView):
    pass

# def homepage(request):
#     if request.method == "POST":
#         form = SearchFrom(request.form)
#         if form.is_valid():
#             return HttpResponseRedirect("/")
#     else:
#         form = SearchForm()
#         return render(request, 'index.html', {"logged_in": request.user.is_authenticated(), "form": form})

def logout_user(request):
    print("hi")
    #logout(request)
    return homepage(request)

def search(request):
    pass

class ExampleView(TemplateView):
    template_name = "example.html"

    def get_context_data(self, **kwargs):
        context = super(ExampleView, self).get_context_data(**kwargs)
        context["title"] = self.request.GET["title"]
        context["content"] = Example.objects.filter(title=self.request.GET["title"]).all()[0].content
        return context

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
    print request.POST
    title = request.POST['title']
    topic = Topic.objects.get(name=request.POST['topic'])
    concept = Concept.objects.get(name=request.POST['concept'])
    content = request.POST['content']
    email = request.POST['email']

    print "Title: %s, Topic: %s, Concept: %s, Content: %s, Email: %s" % (title, topic, concept, content, email)

    Example(title=title, topic=topic, concept=concept, content=content, email=email).save()
    return render(request, 'question_asked.html')
