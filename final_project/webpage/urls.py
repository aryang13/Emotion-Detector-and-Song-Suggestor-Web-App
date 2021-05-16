from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('music/', views.music, name='music'),
    path('about/', views.about, name='about'),
]