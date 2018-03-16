from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Image, Profile, Comment, User
from django.views.generic import RedirectView
from . forms import NewCommentForm, NewStatusForm, UserForm , ProfileForm , PostPictureForm
from django.db import transaction


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    title='Welcome to Instagram'
    img = Image.this_image()
    profile = Profile.get_profile()
    current_user = request.user
    
    return render(request,'index.html',{"img":img, "profile":profile})

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
    profiles = Profile.objects.filter(user_id=request.user.id)

    
    return render(request,'profile.html',{"title":title,"profiles":profiles})


@login_required
@transaction.atomic
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@login_required(login_url='/accounts/login/')
def post_picture(request):
    test = 'Working'
    current_user = request.user
    profiles = Profile.objects.all()
    for profile in profiles:
        if profile.user.id == current_user.id:
            if request.method == 'POST':
                form = PostPictureForm(request.POST, request.FILES)
                if form.is_valid():
                    post = form.save(commit=False)
                    post.username = current_user
                    post.profile = profile
                    post.save()
                    return redirect('home')
            else:
                form = PostPictureForm()
                content = {
                    "test": test,
                    "post_form": form,
                    "user": current_user
                }
    return render(request, 'post_picture.html')

