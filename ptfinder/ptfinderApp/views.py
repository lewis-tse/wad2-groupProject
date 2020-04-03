from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views import View
from ptfinderApp.forms import UserForm, UserProfileForm, TrainerProfileForm, CreateBookingForm
from ptfinderApp.models import UserProfile, Booking, Gym, Trainer

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
    
    registered = False
    if request.method == 'POST':
        userForm = UserForm(request.POST)
        userProfileForm = UserProfileForm(request.POST)

        print(userForm.is_valid())
        print(userProfileForm.is_valid())

        if userForm.is_valid() and userProfileForm.is_valid():
            user = userForm.save()
            if user.cleaned_data['password'] == user.cleaned_data['conpass']:
                user.set_password(user.password)
                user.save()

            userProfile = userProfileForm.save(commit=False)
            userProfile.account = user

            if 'img' in request.FILES:
                userProfile.img = request.FILES['img']

            userProfile.save()
            registered = True
        else:
            print(userForm.errors, userProfileForm.errors)

    context_dict = {'base_user_form': userForm, 'user_form': userProfileForm, 'registered': registered}

    return render(request, 'ptfinderApp/register.html', context=context_dict)

def trainer_register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        trainer_form = TrainerProfileForm(request.POST)
        
        if user_form.is_valid() and trainer_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            trainer = trainer_form.save(commit=False)
            trainer.t_account = user
            
            if 'picture' in request.FILES:
                trainer.picture = request.FILES['picture']
                
            trainer.save()
            registered = True
        else:
            print(user_form.errors, trainer_form.errors)
    else:
        base_user_form = UserForm()
        trainer_form = TrainerProfileForm()
    
    context_dict = {'base_user_form': base_user_form, 'trainer_form': trainer_form,'registered':registered}

    return render(request, 'ptfinderApp/register-trainer.html', context=context_dict)

@login_required
def edit_profile(request, username):
    userprofile = UserProfile.objects.get_or_create(account=request.user)[0]
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST,instance=userprofile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            custom_form = profile_form.save(commit=False)
            custom_form.user = user_form
            custom_form.save()
            return redirect('ptfinder:user')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=userprofile)
            
    context_dict = {'user_form':user_form, 'profile_form':profile_form}

    return render(request, 'ptfinderApp/edit-profile.html', context=context_dict)
    
def gym(request):
#name, owner, city, address_postcode
    context_dict = {}
    
    if request.method == 'POST':
        
        search = request.POST.get('search')
        
        try:
            gyms = Gym.objects.get(name=search)
            if gyms:
                context_dict['gyms'] = gyms
                context_dict['search_type'] = "specific"
                print(context_dict)
                return render(request, 'ptfinderApp/gym.html', context=context_dict)
        except:
            pass
        
        
        try:
            gyms = Gym.objects.filter(owner=search)
            if gyms:
                context_dict['gyms'] = gyms
                context_dict['search_type'] = "generic"
                return render(request, 'ptfinderApp/gym.html', context=context_dict)
        except:
            pass
            
        
        gyms = Gym.objects.filter(address_postcode=search)
        if gyms:
            context_dict['gyms'] = gyms
            context_dict['search_type'] = "generic"
            return render(request, 'ptfinderApp/gym.html', context=context_dict)        
            
        gyms = Gym.objects.filter(city=search) 
        if gyms:
            context_dict['gyms'] = gyms
            context_dict['search_type'] = "generic"
            return render(request, 'ptfinderApp/gym.html', context=context_dict)
        
        return render(request, 'ptfinderApp/gym.html', context=context_dict)
       
    else:
        gyms = Gym.objects.order_by('-name')[:5]
        context_dict['gyms'] = gyms 
        context_dict['search_type'] = "generic"
        return render(request, 'ptfinderApp/gym.html', context=context_dict)
        

def gym_profile(request):
    context_dict = {}

    return render(request, 'ptfinderApp/gym-profile.html', context=context_dict)
    
def contact_us(request):
    context_dict = {}
    
    return render(request, 'ptfinderApp/contact_us.html', context=context_dict)

def book(request):
    context_dict = {}

    return render(request, 'ptfinderApp/book.html', context=context_dict)

@login_required
def create_booking(request, account):
    user_profile = UserProfile.objects.get_or_create(account=request.user)[0]
    
    if request.method == 'POST':
        booking_form = CreateBookingForm(request.POST)
        
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.username = user_profile
            booking.save()
            return redirect('ptfinder:index')
        else:
            print(booking_form.errors)
    else:
        booking_form = CreateBookingForm()
    
    context_dict = {'booking_form':booking_form}
    
    return render(request, 'ptfinderApp/create-booking.html', context=context_dict)

@login_required
def view_bookings(request, uservar):
    context_dict = {}
    
    bookings = Booking.objects.filter(username__account__username=uservar)
    if bookings:
       pass
    else:
        bookings = Booking.objects.filter(t_username__t_account__username=uservar)
  
            
    
    context_dict['bookings'] = bookings
        
    #context_dict
    

    return render(request, 'ptfinderApp/view-bookings.html', context=context_dict)
    
def trainer(request):
    context_dict = {}
    
    if request.method == 'POST':
        search = request.POST.get('search')
        
        try:
            trainers = Trainer.objects.all()
            
            for trainer in trainers:
                if trainer.t_account.username == search:
                    output_trainer = trainer
                    
            if output_trainer:
                context_dict['trainer'] = output_trainer
                print(context_dict)
        except Exception as e:
            print("except")
            print(e)
            pass
        
    return render(request, 'ptfinderApp/trainer.html', context=context_dict)

def trainer_profile(request):
    context_dict = {}

    return render(request, 'ptfinderApp/trainer-profile.html', context=context_dict)

