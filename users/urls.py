from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.login_user, name='users-login'),
    path('register/', views.register, name='users-register'),
    path('logout/', views.logout_user, name='users-logout'),
]
