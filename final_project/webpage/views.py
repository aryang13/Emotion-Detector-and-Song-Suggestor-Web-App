from django.shortcuts import render

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

def homepage(request):
    return render(request, 'webpage/homepage.html')

def about(request):
    return render(request, 'webpage/about.html', {'title': 'About'})

