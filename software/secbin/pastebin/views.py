from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Bopie
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
import short_url
from django.shortcuts import get_object_or_404
from .base_62_converter import *
from random import randint
# Create your views here.

#home page
def index(request):
    context = {
        'posts': Bopie.objects.all()
    }

    return render(request, 'pastebin/index.html', context)

class PostListView(ListView):
    model = Bopie
    template_name = 'pastebin/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted'] #views them from newest to oldest
    paginate_by = 10

class PostDetailView(DetailView):    
#    model = get_object_or_404(Bopie)
 #   model = Bopie.objects.all()
     model = Bopie
    


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Bopie
    fields = ['title', 'content']
    
    def form_valid(self, form):
        model = Bopie
        form.instance.author = self.request.user
        form.instance.slug = dehydrate(randint(100000000,9999999999))
        print(form.instance.slug)
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Bopie
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        bopie = self.get_object()

        if self.request.user == bopie.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Bopie

    success_url = '/'
    def test_func(self):
        bopie = self.get_object()

        if self.request.user == bopie.author:
            return True
        return False
    


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
