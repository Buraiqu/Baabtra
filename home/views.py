from django.shortcuts import render

# Create your views here.
def home_home(request):
    return render(request,'home_templates/home.html')