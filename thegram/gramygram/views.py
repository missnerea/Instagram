from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Image


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    title='Welcome to Instagram'
    img = Image.this_image()

    return render(request,'index.html',{"img":img})

 