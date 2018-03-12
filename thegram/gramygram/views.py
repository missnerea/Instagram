from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Image
from django.views.generic import RedirectView


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    title='Welcome to Instagram'
    img = Image.this_image()

    return render(request,'index.html',{"img":img})

class ImageLikeToggle(RedirectView):
     def get_redirect_url(self, *args, **kwargs):
        slug = self.kwargs.get("slug")
        print(slug)
        obj = get_object_or_404(Post, slug=slug)
        url_ = obj.get_absolute_url()
        user = self.request.user
        if user.is_authenticated():
            if user in obj.likes.all():
                obj.likes.remove(user)
            else:
                obj.likes.add(user)
        return url_