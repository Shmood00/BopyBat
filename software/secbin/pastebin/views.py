from django.shortcuts import render
from .models import Bopie

# Create your views here.

def index(request):
    context = {
        'posts': Bopie.objects.all()
    }

    return render(request, 'pastebin/index.html', context)

def login(request):
    return render(request, 'pastebin/login.html', {'title':'Login'})


