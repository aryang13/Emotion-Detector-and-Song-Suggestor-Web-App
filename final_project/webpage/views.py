from django.shortcuts import render
from django.http import HttpResponse
import base64
import numpy as np
import cv2
from django.views.generic import TemplateView

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

class Home(TemplateView):
    template_name = 'webpage/base.html'

# def home(request):
#     context = {
#         'songs': songs
#     }
#     return render(request, 'webpage/home.html', context)

def about(request):
    return render(request, 'webpage/about.html', {'title': 'About'})

def my_image(request):

    data_uri = request.POST.get('imageData')

    if data_uri != None:
        __, encoded = data_uri.split(",", 1)
        
        data = base64.b64decode(encoded)
        im_arr = np.frombuffer(data, dtype=np.uint8)
        img = cv2.imdecode(im_arr, flags=cv2.IMREAD_COLOR)

        write_image(img)
        return about(request)
        
    return render(request, 'webpage/home.html')

def write_image(image):
    cv2.imwrite("webpage\\images\\image.png", image)