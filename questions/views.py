from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Question
from django.utils import timezone
# Create your views here.
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Choice, Question
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.db import models
from django.views.generic import View
from questions.forms import QuestionForm


class CreateQuestionView(View):

    def get(self, request):
        form = QuestionForm(author=request.user)
        return render(request, 'questions/create.html', {'form': form})

    def question(self, request):
        form = QuestionForm(data=request.POST, author=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home:index'))
        return render(request, 'questions/create.html', {'form': form})


class EditQuestionView(View):

    def get(self, request, pk):
        try:
            question = Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            raise Http404
        form = QuestionForm(instance=question ,author=request.user)
        return render(request, 'questions/edit.html', {'form': form, 'pk': pk})

    def question(self, request, pk):
        try:
            question = Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            raise Http404
        form = QuestionForm(instance=question, author=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home:index'))
        return render(request, 'questions/edit.html', {'form': form, 'pk': pk})


class IndexView(generic.ListView):
    template_name = 'questions/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
  	 return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'questions/detail.html'
    def detail_view(request, object_id=None):
        if request.user.is_authenticated():
            question = get_object_or_404(Question, id=object_id)
        template = "questions/detail.html"
        context = {
            "object": question
        }
        return render(request, template, context)


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'questions/results.html'

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)