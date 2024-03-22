from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="music_recommender-home"),
    path('about/', views.about, name="music_recommender-about"),
]