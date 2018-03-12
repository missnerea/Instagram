from django import forms
from .models import Image, Comment
#......
class NewStatusForm(forms.ModelForm):
    class Meta:
      model=Image 
      fields=('image_image','caption')

class NewCommentForm(forms.ModelForm):
    class Meta:
     models=Comment
     fields=('comment',)   