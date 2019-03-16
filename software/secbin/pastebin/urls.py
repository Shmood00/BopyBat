from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
import short_url
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='pastebin-index'),
    path('post/new/', PostCreateView.as_view(), name='bopie-create'),
    path('post/<str:slug>/download/', views.downloadBopie, name='bopie-download'),
    
    path('post/<str:slug>/', PostDetailView.as_view(), name='bopie-detail'),
    path('post/<str:slug>/update/', PostUpdateView.as_view(), name='bopie-update'),
    path('results/', views.search, name='search'),
    path('post/<str:slug>/delete/', PostDeleteView.as_view(), name='bopie-delete'),
    path('login/', auth_views.LoginView.as_view(template_name='pastebin/login.html'), name='pastebin-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='pastebin/logout.html'), name='pastebin-logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='pastebin/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='pastebin/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='pastebin/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='pastebin/password_reset_complete.html'), name='password_reset_complete'),
    path('register/', views.register, name='pastebin-register'),
    path('profile/', views.profile, name='pastebin-profile'),
]
