from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Image, Profile, Comment, User
from django.views.generic import RedirectView
from . forms import NewCommentForm, NewStatusForm


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

@login_required(login_url='/accounts/login')
def new_status(request):
    current_user= request.user
    if request.method == 'POST':
       form =  NewStatusForm(request.POST, request.FILES) 
       if form.is_valid():
        status = form.save(commit=False)
        status.editor=current_user
        status.save()

    else:
        form= NewStatusForm()
        return render (request,'new_status.html',{"form":form})

def post_comment(request,id):
    title = 'new comment'
    post = get_object_or_404(Image, id=id)
    current_user = request.user
    if request.method == 'POST':
        form = NewCommentForm(request.POST)
        if form.is_valid():
            post_comment = form.save(commit=False)
            post_comment.user = current_user
            post_comment.pic = post
            post_comment.save()
            return redirect('index')
    else:
        form = CommentForm()
        
    return render(request,'new_comment.html',{"title":title,"form":form})

@login_required(login_url='/accounts/login/')
def profile(request):
    title = 'User Profile'
    try:
        profiles = Profile.objects.filter()
        photos = Image.objects.filter()
    except Image.DoesNotExist:
        raise Http404
    return render(request,'profile.html',{"title":title,"profiles":profiles,"photos":photos})
