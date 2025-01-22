from django.shortcuts import render 

def index(request):
    return render(request, 'ii/index.html')