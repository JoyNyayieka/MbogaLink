from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about-us.html')

def contact(request):
    return render(request,'contact-us.html')

def typography(request):
    return render(request,'typography.html')