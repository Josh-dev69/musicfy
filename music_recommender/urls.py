from django.urls import path
from . import views

urlpatterns = [
    path('', views.generate_recommendations, name="musicify-home"),
    path('about/', views.about, name="musicify-about"),
]