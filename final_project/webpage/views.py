from django.shortcuts import render
from django.http import HttpResponse
import base64
import numpy as np
from django.views.generic import TemplateView
import requests, re, time
import torch, torchvision
from torch import nn, optim
from torchvision import datasets, models, transforms
import tensorflow as tf
from PIL import Image
from mtcnn import MTCNN
import cv2
import os

#The MTCNN takes as a input a single image and outputs the bounding box coordinates for that image where the face is.
#The code below takes in an input directory and runs the MTCNN on all the images in that directory and outputs in
#output directory only the bounded images (only faces).
#link to code below: https://stackoverflow.com/questions/65105644/how-to-face-extraction-from-images-in-a-folder-with-mtcnn-in-python
def crop_image(source_dir, dest_dir, mode):
    if os.path.isdir(dest_dir)==False:
        os.mkdir(dest_dir)
    detector = MTCNN()
    source_list=os.listdir(source_dir)
    uncropped_file_list=[]
    for f in source_list:
        f_path=os.path.join(source_dir, f)
        dest_path=os.path.join(dest_dir,f)
        img=cv2.imread(f_path)
        try:
            data=detector.detect_faces(img)
        except:
            print(f_path)
            data==[]
            pass
        if data ==[]:
            uncropped_file_list.append(f_path)
        else:
            if mode==1:  #detect the box with the largest area
                for i, faces in enumerate(data): # iterate through all the faces found
                    box=faces['box']  # get the box for each face
                    biggest=0
                    area = box[3]  * box[2]
                    if area>biggest:
                        biggest=area
                        bbox=box
                bbox[0]= 0 if bbox[0]<0 else bbox[0]
                bbox[1]= 0 if bbox[1]<0 else bbox[1]
                img=img[bbox[1]: bbox[1]+bbox[3],bbox[0]: bbox[0]+ bbox[2]]
                cv2.imwrite(dest_path, img)
            else:
                for i, faces in enumerate(data): # iterate through all the faces found
                    box=faces['box']
                    if box !=[]:
                        # return all faces found in the image
                        box[0]= 0 if box[0]<0 else box[0]
                        box[1]= 0 if box[1]<0 else box[1]
                        cropped_img=img[box[1]: box[1]+box[3],box[0]: box[0]+ box[2]]
                        fname=os.path.splitext(f)[0]
                        fext=os.path.splitext(f)[1]
                        fname=fname + str(i) + fext
                        save_path=os.path.join(dest_dir,fname )
                        cv2.imwrite(save_path, cropped_img)

    return uncropped_file_list

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
    source_dir = 'webpage/images'
    dest_dir = 'webpage/faceonly'
    uncropped_files_list=crop_image(source_dir, dest_dir,1)

def music(request, img):
    write_image(img)
    model=torch.load('projectmod',map_location=torch.device('cpu'))
    model.eval()
    xform = transforms.Compose([transforms.Resize((224, 224)), transforms.ToTensor()])
    img=Image.open('webpage\\faceonly\\image.png')
    data = xform(img)
    output = model(data[None, ...])
    preds=torch.max(output.detach(), 1)[1].item()
    if(preds==0):
        #return angry list
        return render(request,'webpage/music.html', {'mood': 'Angry', 'playlist': 'playlist/5XBvBzMBRcdCrKUAs5VoR4'})
    if(preds==1):
        #return happy list
        return render(request,'webpage/music.html', {'mood': 'Happy', 'playlist': 'playlist/14FMPAe3yffuI47MUX3Alg'})
    if(preds==2):
        #return neutral list
        return render(request,'webpage/music.html', {'mood': 'Neutral', 'playlist': 'playlist/31n4J7BzWnoOPLuTCyZYRv'})
    if(preds==3):
        #return sad list
        return render(request,'webpage/music.html', {'mood': 'Sad', 'playlist': 'playlist/42zINuckj3dU1CHcGBSrwk'})

def about(request):
    return render(request, 'webpage/about.html', {'title': 'About'})
