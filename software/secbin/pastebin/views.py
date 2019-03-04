from django.shortcuts import render, redirect
from .models import Bopie
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.

#home page
def index(request):
    context = {
        'posts': Bopie.objects.all()
    }

    return render(request, 'pastebin/index.html', context)

def about(request): #will actually login TBH IDK IF THIS IS NEEDED
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

    return render(request, 'pastebin/register.html', {'form':form, 'title':'Register'})

@login_required #user must be logged in to access this page
def profile(request):

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            
            messages.success(request, 'Your account has been updated.')
            return redirect('pastebin-profile')
   
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'pastebin/profile.html', context)