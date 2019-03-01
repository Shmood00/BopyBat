from django.shortcuts import render, redirect
from .models import Bopie
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.

#home page
def index(request):
    context = {
        'posts': Bopie.objects.all()
    }

    return render(request, 'pastebin/index.html', context)

def about(request): #will actually login
    return render(request, 'pastebin/about.html', {'title':'About'})

#registration
def register(request):
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save() #saves new user
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your account has been created. You are now allowed to login.')

            return redirect('pastebin-login')
    else:
        form = UserRegisterForm()

    return render(request, 'pastebin/register.html', {'form':form})

