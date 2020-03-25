from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {}

    return render(request, 'ptfinderApp/index.html', context=context_dict)

def profile(request):
    context_dict = {}

    return render(request, 'ptfinderApp/profile.html', context=context_dict)
