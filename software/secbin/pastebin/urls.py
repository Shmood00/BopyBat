from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='pastebin-index'),
    path('login/', views.login, name='pastebin-login')
]