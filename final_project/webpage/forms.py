from django import forms

from .models import Image_parsed


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image_parsed
        fields = ['hidden_form']
        widgets = {'hidden_form': forms.HiddenInput()}