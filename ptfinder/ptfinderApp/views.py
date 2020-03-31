from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
    context_dict = {}

    return render(request, 'ptfinderApp/index.html', context=context_dict)

def user(request):
    context_dict = {}

    return render(request, 'ptfinderApp/user.html', context=context_dict)

def user_profile(request):
    context_dict = {}

    return render(request, 'ptfinderApp/user-profile.html', context=context_dict)
    
def login(request):
    context_dict = {}

    return render(request, 'ptfinderApp/login.html', context=context_dict)
    
def register(request):
    context_dict = {}

    return render(request, 'ptfinderApp/register.html', context=context_dict)
    
def trainer_register(request):
    context_dict = {}

    return render(request, 'ptfinderApp/trainer_register.html', context=context_dict)

def edit_profile(request):
    context_dict = {}

    return render(request, 'ptfinderApp/edit-profile.html', context=context_dict)
    
def gym(request):
    context_dict = {}

    return render(request, 'ptfinderApp/gym.html', context=context_dict)

def gym_profile(request):
    context_dict = {}

    return render(request, 'ptfinderApp/gym-profile.html', context=context_dict)
    
def contact_us(request):
    context_dict = {}

    return render(request, 'ptfinderApp/contact-us.html', context=context_dict)

def book(request):
    context_dict = {}

    return render(request, 'ptfinderApp/book.html', context=context_dict)

def create_booking(request):
    context_dict = {}

    return render(request, 'ptfinderApp/create-booking.html', context=context_dict)

def view_bookings(request):
    context_dict = {}

    return render(request, 'ptfinderApp/view-bookings.html', context=context_dict)
    
def trainer(request):
    context_dict = {}

    return render(request, 'ptfinderApp/trainer.html', context=context_dict)

def trainer_profile(request):
    context_dict = {}

    return render(request, 'ptfinderApp/trainer-profile.html', context=context_dict)

