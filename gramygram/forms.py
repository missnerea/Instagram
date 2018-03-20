from django import forms
from .models import Image, Comment , User , Profile
#......
class NewStatusForm(forms.ModelForm):
    class Meta:
      model=Image 
      fields=('image_image','caption')

class NewCommentForm(forms.ModelForm):
    class Meta:
     model=Comment
     fields=('comments',)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_picture', 'bio', 'email')

class PostPictureForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['caption', 'image_image']