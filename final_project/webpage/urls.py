from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('music/', views.music, name='music'),
    path('about/', views.about, name='about'),
   # path('', views.home, name='webpage-home'),
    # path('', views.my_image, name='webpage-home'),
    # path('my_image/', views.my_image, name='main'),
]