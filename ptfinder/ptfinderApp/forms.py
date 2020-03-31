from django import forms
from django.contrib.auth.models import User
from ptfinderApp.models import UserProfile, Trainer

class UserForm(forms.ModelForm):
        password = forms.CharField(widget=forms.PasswordInput())
        
        class Meta:
            model = User
            fields = ('username','first_name','last_name','email','password',)
            
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('experience','sex','location','img',)
        
class TrainerProfileForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ('g_id','contact_no','specialism','sex','img','price',)
        
class CreateBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('username', 't_username', 'datetime', 'location',)