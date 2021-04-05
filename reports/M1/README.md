# Milestone M1 report
## Current state

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;We are currently on track of what was stated for Milestone 1 in the project proposal. No changes were made to the prosopal as the team deemed the goals for this milestone were attainable. Throughout the week we were able to create the dataset, create a model, build a django framework and deploy it on google cloud. 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The dataset that we created contains 4 different emotions: happy, sad, angry, and neutral. The dataset was created using Bing-Bulk-Image-Downloader (https://github.com/ostrolucky/Bulk-Bing-Image-downloader), where we were we able to attain around 500-600 images for each emotion after taking out rejects. The rejects were eliminated due to various reasons and were hand selected based on judgement of the student. The folders were saved on github and are accessible by anyone on the repo. The code for the extraction of the dataset is written in the Datacreation.ipynb.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The model was created using similar principles to assignment 2. The model has been tested using the datasets that were discussed above. We are currently able to achieve a accurracy of 80% using the first model created. The goal in the future is to achieve an accuracy of 90-95% by the end of the project. The model code is written in ModelSkeleton.ipynb.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For the web framework it was decided to use django due to its simplicity on creating websites. Currently a frontend has been created where you are able to go to different pages from a navbar. In addition the website is able to access your webcam and take photos of your face when the capture button is pressed.  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

////////// in progress //////////////

## Current challenges

## Team member's tasks
### 1. Deepan Chakravarthy
I was responsible for the skeleton code of the model and training of the dataset. The prepared dataset was loaded with the appropriate labels and transformed. As we are applying transfer learning, a pretrained resnet18 was loaded with no modifications to the layers yet. this was done to check the accuracy of the model given a raw resnet18. Since this is a classification task, crossentropy loss was used for training.
A test accuracy of 85% was acheived after 10 epochs. I am currently working on modifying the FC layers and validating the code. 
### 2. Aryan Gandhi
### 3. Steve He
Since we are planning to host the website using google cloud service, I have tried to deploy some simple (non-ML related) dynamic website using through Django. And users are able to visit our website given the public address of our hosting machien.
Also, I tried to run through some simple ML project like perceptron on the cloud Linux VM and it went well (meaning we can do computation on the cloud machine).
reference:
https://heartbeat.fritz.ai/deploying-machine-learning-models-on-google-cloud-platform-gcp-7b1ff8140144
https://medium.com/analytics-vidhya/deploying-deep-learning-django-app-to-google-cloud-platform-70bab374704c
### 4. Arya Phan
Arya was responsible for srcaping images online and creating the dataset. She collected all images for the four emotions by using Bing image scraping tools and then manually went through each folder to make sure all images that are duplicated or not appropriate for the project were screened out. Arya is currently drafting the frontend of our webpage using HTML and CSS. Additionally, she is also researching output songs that correspond to each emotion together with the team.
