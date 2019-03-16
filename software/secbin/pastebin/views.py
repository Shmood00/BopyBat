from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Bopie
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, DateField, postUpload
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, HttpResponse
from .base_62_converter import *
from random import randint
import requests, os
from django.core.paginator import Paginator
from django.db.models import Q
from datetime import datetime, timedelta
from django.core.files.storage import FileSystemStorage
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
    #ordering = ['-date_posted'] #views them from newest to oldest
    paginate_by = 10


    def get_queryset(self):


        return Bopie.objects.filter(
            Q(
                Q(date_expiry__gt=datetime.now()) & Q(disable_bopie=False)
            ) |
            Q(
                Q(date_expiry=None) & Q(disable_bopie=False)
            )
            ).order_by('-date_posted')


class PostDetailView(DetailView):
     model = Bopie
    
class PostCreateView(LoginRequiredMixin, CreateView): #Displays the form for user to create a new Bopie (post)
    model = Bopie
    
    fields = ['title', 'postUpload','content', 'date_expiry']
    
    def form_valid(self, form):
        model = Bopie
        
        form.instance.author = self.request.user
        form.instance.slug = dehydrate(randint(100000000,9999999999))
        
        return super().form_valid(form)

# Display form to update existing Bopie (post)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Bopie
    fields = ['title', 'postUpload','content', 'date_expiry']

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


#Function that handles searching
def search(request):
    template = "pastebin/index.html"
    query = request.GET.get('q')

    if query:
        results = Bopie.objects.filter(
            Q(
                Q( 
                    Q(content__icontains=query)|
                    Q(title__icontains=query)|
                    Q(author__username__iexact=query) |
                    Q(date_expiry=None)
                )

                & 

                Q(
                    Q(date_expiry__gt=datetime.now()) &
                    Q(disable_bopie=False)
                )
            ) |
            Q(
                Q(
                    Q(content__icontains=query)|
                    Q(title__icontains=query)|
                    Q(author__username__iexact=query)
                    
                )
                &
                Q(
                    
                    Q(date_expiry=None) &
                    Q(disable_bopie=False)
                )
                
            )
        ).order_by('-date_posted')
        
        
        context = {
        'posts':results
        }
        
        
        return render(request, template, context)
    else:
        return redirect('/')

#Downloads the post 
def downloadBopie(request, slug):
    model = Bopie.objects.get(slug = slug)
    filename = slug
    content = str(model.content)
    response = HttpResponse(content, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename{0}'.format(filename)

    return response



#Function that handles user registration
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



#Function that handles user Profile
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


