from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req,'index.html')
def new1(req):
    return render(req,'new1.html')