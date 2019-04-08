from django.shortcuts import render

# Create your views here.

def cvPageView(request):
    return render(request, 'cv/index.html')