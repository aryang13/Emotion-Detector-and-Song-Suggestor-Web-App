from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

songs = [
    {
        'title': 'Party in the USA',
        'singer': 'Miley Cyrus',
    },
    {
        'title': 'Wet Dreamz',
        'singer': 'J. Cole',
    },
]

def home(request):
    context = {
        'songs': songs
    }
    return render(request, 'webpage/home.html', context)

def about(request):
    return render(request, 'webpage/about.html', {'title': 'About'})

def my_image(request):
    print("--------------------------------------")
    print(request.GET.get('taken_image'))
    print("--------------------------------------")
    return HttpResponse('')

