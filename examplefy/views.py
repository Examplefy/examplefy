from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

from .models import Example

# Create your views here.
def homepage(request):
    return render(request, 'index.html', {"logged_in": request.user.is_authenticated()})

def logout_user(request):
    print("hi")
    #logout(request)
    return homepage(request)
