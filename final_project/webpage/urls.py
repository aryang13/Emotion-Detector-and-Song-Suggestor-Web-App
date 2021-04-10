from django.urls import path
from . import views

urlpatterns = [
   # path('', views.home, name='webpage-home'),
    path('', views.homepage, name='homepage'),
    path('about/', views.about, name='webpage-about'),
]