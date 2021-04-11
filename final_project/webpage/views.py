from django.shortcuts import render
from django.http import HttpResponse
import base64
import numpy as np
import cv2
from django.views.generic import TemplateView
import requests, re, time
import torch, torchvision
from torch import nn, optim
from torchvision import datasets, models, transforms
# Create your views here.

def homepage(request):

    data_uri = request.POST.get('imageData')

    if data_uri != None:
        __, encoded = data_uri.split(",", 1)

        data = base64.b64decode(encoded)
        im_arr = np.frombuffer(data, dtype=np.uint8)
        img = cv2.imdecode(im_arr, flags=cv2.IMREAD_COLOR)
        return music(request, img)

    return render(request, 'webpage/homepage.html')

def write_image(image):
    cv2.imwrite("webpage\\images\\image.png", image)

def music(request, img):
    write_image(img)
    model=torch.load('final_project/projectmod',map_location=torch.device('cpu'))
    model.eval()
    xform = transforms.Compose([transforms.Resize((224, 224)), transforms.ToTensor()])
    data = xform(img)
    output = model(data[None, ...])
    preds=torch.max(output.detach(), 1)[1].item()
    if(preds==0):
        #return angry list
        return render(request,'webpge/music.html')
    if(preds==1):
        #return happy list
        return render(request,'webpge/music.html')
    if(preds==2):
        #return neutral list
        return render(request,'webpge/music.html')
    if(preds==3):
        #return sad list
        return render(request,'webpge/music.html')

def about(request):
    return render(request, 'webpage/about.html', {'title': 'About'})
