from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='webpage-home'),
    path('about/', views.about, name='webpage-about'),
    path('my_image/', views.my_image),
]