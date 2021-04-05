# Milestone M1 report
## Current state

Our team created a dataset with 4 classes representing 4 basic human emotions: happy, sad, angry and neutral. Each emotion has around 500-600 images after considering rejects. We were able to eliminate all duplicated and irrelevant images by using web scraping tools and also by manually double checking that all images are unique and appropriate for the project. All images were scraped from Bing and saved in folders that serve as our class labels inside the "dataset" directory (please see Datacreation.ipynb notebook for the code). 



## Team member's tasks
### 1. Deepan Chakravarthy
was responsible for the skeleton code of the model and training of the dataset. The prepared dataset was loaded with the appropriate labels and transformed. As we are applying transfer learning, a pretrained resnet18 was loaded with no modifications to the layers yet. this was done to check the accuracy of the model given a raw resnet18. Since this is a classification task, crossentropy loss was used for training.
A test accuracy of 85% was acheived after 10 epochs. I am currently working on modifying the FC layers and validating the code. 
### 2. Aryan Gandhi
### 3. Steve He
Since we are planning to host the website using google cloud service, I have tried to deploy some simple (non-ML related) dynamic website using through Django. And users are able to visit our website given the public address of our hosting machien.
Also, I tried to run through some simple ML project like perceptron on the cloud Linux VM and it went well (meaning we can do computation on the cloud machine).
reference:
https://heartbeat.fritz.ai/deploying-machine-learning-models-on-google-cloud-platform-gcp-7b1ff8140144
https://medium.com/analytics-vidhya/deploying-deep-learning-django-app-to-google-cloud-platform-70bab374704c
### 4. Arya Phan
Arya was responsible for srcaping images online and creating the dataset. She collected all images for the four emotions by using Bing image scraping tools and then manually went through each folder to make sure all images that are duplicated or not appropriate for the project were screened out. Arya is currently drafting the frontend of our webpage using HTML and CSS. 
