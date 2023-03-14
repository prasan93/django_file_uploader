
# import form class from django
from django import forms
from .models import image_uploader
 
# create a ModelForm
class ImageForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = image_uploader
        fields = "__all__"