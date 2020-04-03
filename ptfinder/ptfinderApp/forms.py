from PIL import Image
from django import forms
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from ptfinderApp.models import UserProfile, Trainer, Booking, Gym
import datetime


class UserForm(forms.ModelForm):
        
    username = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}), required=True)
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bob'}), required=True)
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ross'}), required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'aria-describedby': 'userPassHelp'}), required=True)
        
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password',)
            
class UserProfileForm(UserForm):
    conPass = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
    experience = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'e.g. None, 1 Year etc.', 'aria-required': 'false', 'rows':'3', 'cols': '3'}))    
    location = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Glasgow', 'aria-describedby': 'userLocationHelp'}))
    sex = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sex'}))
    img = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file', 'accept': '.jpg, .jpeg, .png, image/jpeg, image/png', 'aria-required': 'false'}), required=False)
    
    class Meta:
        model = UserProfile
        fields = ('experience','sex','location','img',)
        
class TrainerProfileForm(UserForm):
    conPass = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
    sex = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sex'}))
    img = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file', 'accept': '.jpg, .jpeg, .png, image/jpeg, image/png', 'aria-required': 'false'}))
    contact_no = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+44 7123 456 789'}))
    specialism = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'e.g. None, 1 Year etc.', 'aria-required': 'false', 'rows':'3', 'cols': '3'}))
    price = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hourly/Session Charge'}))
    
    gyms = Gym.objects.all()
    gym_data = [(gym.g_id, gym.name) for gym in gyms]
    g_id = forms.ChoiceField(choices=gym_data, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Trainer 
        fields = ('g_id','contact_no','specialism','sex','img','price',)
        
class CreateBookingForm(forms.ModelForm):
    datetime = forms.DateTimeField(help_text="[yyyy-mm-dd HH:MM]", initial=datetime.datetime.now())
    
    class Meta:
        model = Booking
        fields = ('username','trainer_username', 'datetime', 'location',)