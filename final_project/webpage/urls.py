from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_image, name='webpage-home'),
    # path('my_image/', views.my_image, name='main'),
    path('about/', views.about, name='webpage-about'),
]