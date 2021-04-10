from django.db import models

# Create your models here.
class Image_parsed(models.Model):
    hidden_form = models.CharField(max_length=255)