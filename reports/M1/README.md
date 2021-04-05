# Milestone M1 report
## Current state

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;We are currently on track of what was stated for Milestone 1 in the project proposal. No changes were made to the prosopal as the team deemed the goals for this milestone were attainable. Throughout the week we were able to create the dataset, create a model, build a django framework and deploy it on google cloud. 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The dataset that we created contains 4 different emotions: happy, sad, angry, and neutral. The dataset was created using Bing-Bulk-Image-Downloader (https://github.com/ostrolucky/Bulk-Bing-Image-downloader), where we were we able to attain around 500-600 images for each emotion after taking out rejects. The rejects were eliminated due to various reasons and were hand selected based on judgement of the student. The folders were saved on github and are accessible by anyone on the repo. The code for the extraction of the dataset is written in the Datacreation.ipynb.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The model was created using similar principles to assignment 2. The model has been tested using the datasets that were discussed above. We are currently able to achieve a accurracy of above 80% using the first model created. The goal in the future is to achieve an accuracy of 90-95% by the end of the project. The model code is written in ModelSkeleton.ipynb.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For the web framework it was decided to use django due to its simplicity on creating websites. Currently a frontend has been created where you are able to go to different pages from a navbar. In addition the website is able to access your webcam and take photos and display it below the button when the capture button is pressed. 

![alt text](https://github.com/UBC-CPEN291/project-team-allosaurus/blob/main/reports/M1/currentwebsite.png)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For deploying of the website we decided to use google cloud due to us having credits and it having many different features that we needed. So far we have been able to set up an instance that allows for the google cloud to deploy the django webpage for anyone to access with the link is provided. Some problems that occurred when trying to deploy it was mainly when we tried to allow webcam access to the user, however are fixing the app.yaml and the settings.py file we were able to get everything working. In order to deploy the django application we use the googl cloud documwentation (https://cloud.google.com/python/django/appengine#windows_1). 

## Current challenges

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Currently we have not been faced with any bottlenecks or challeneges and have been able to complete everything aimed to be finished for milestone 1 in the allocated time.

## Team member's tasks
### 1. Deepan Chakravarthy

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;I was responsible for the skeleton code of the model and training of the dataset. The prepared dataset was loaded with the appropriate labels and transformed. As we are applying transfer learning, a pretrained resnet18 was loaded with no modifications to the layers yet. this was done to check the accuracy of the model given a raw resnet18. Since this is a classification task, crossentropy loss was used for training.
A test accuracy of 85% was acheived after 10 epochs. 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The future tasks for me is to modify the FC layers in order to gain higher accuracy and validate the code. 

### 2. Aryan Gandhi

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;I was assigned with completed the starting to create the django architecture and begin the webpage. For this milestone, I was learning how to use Django and was able to start the django framework and begin to create a website to use. I created the website using HTML, CSS, and JS. In addition, I completed the use of the website being able to use the webcam to take pictures of the user when the button is pressed. As well, I created the google cloud instance for the django app and was able to deploy it for anybody to view with the provided link. 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The future task for me is to be able to allow the backend to take the picture from the webcam and allow the model to use it. As well begin writing code in order for the backend to send a list of songs based on the mood determined by the ML model. 

### 3. Steve He

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Since we are planning to host the website using google cloud service, I have tried to deploy some simple (non-ML related) dynamic website using through Django. And users are able to visit our website given the public address of our hosting machine.
Also, I tried to run through some simple ML project like perceptron on the cloud Linux VM and it went well (meaning we can do computation on the cloud machine).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The future tasks include taking the image of the person from the website and running the model on the image and returning the output to the website by using google cloud or other services needed. 

References:
- https://heartbeat.fritz.ai/deploying-machine-learning-models-on-google-cloud-platform-gcp-7b1ff8140144
- https://medium.com/analytics-vidhya/deploying-deep-learning-django-app-to-google-cloud-platform-70bab374704c

### 4. Arya Phan
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;I was responsible for scraping images of Bing and creating the dataset. I collected all the images for the four emotions by using the Bing image scraping tools and then manually went through each folder to make sure all images that were duplicates or not appropriate for the project were screened out. 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The future tasks include drafting the frontend of our webpage and using HTML and CSS to design it. Additionally, she is also researching output songs that correspond to each emotion.
