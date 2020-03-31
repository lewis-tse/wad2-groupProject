from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from ptfinderApp.forms import UserForm, UserProfileForm, TrainerProfileForm

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
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.account = user
            
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
                
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    
    context_dict = {'user_form':user_form,'profile_form':profile_form,'registered':registered}
    
    return render(request, 'ptfinderApp/register.html', context=context_dict)

def trainer_register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = TrainerProfileForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.t_account = user
            
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
                
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = TrainerProfileForm()
    
    context_dict = {'user_form':user_form,'profile_form':profile_form,'registered':registered}

    return render(request, 'ptfinderApp/trainer-register.html', context=context_dict)

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

