from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    title='Welcome to Instagram'

    return render(request,'index.html')