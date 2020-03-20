from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class UserProfile(models.Model):
    account = models.OneToOneField(User, on_delete=models.CASCADE)
    
    #Commented lines are not needed if we use the line above, but that means we
    #need to change the names of the fields elsewhere in the code
    
    #username = models.CharField(max_length=30, unique=True)
    #firstname = models.CharField(max_length=20)
    #surname = models.CharField(max_length=20)
    #email = models.EmailField()
    experience = models.CharField(max_length=512)
    sex = models.CharField(max_length=16) 
    location = models.CharField(max_length=30)
    img = models.ImageField(upload_to='userProfile_images',blank=True)
    
    def __str__(self):
        return self.account.username
        
class Gym(models.Model):
    name = models.CharField(max_length=20)
    owner = models.CharField(max_length=20)
    address_line1 = models.CharField(max_length=20)
    address_line2 = models.CharField(max_length=20)
    address_postcode = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    images = models.ImageField(upload_to='gym_images',blank=True)
    description = models.CharField(max_length=512)
    
    @property
    def g_id(self):
        return self.id
   
    def __str__(self):
        return str(self.g_id) + ": " + self.name
        
class Trainer(models.Model):
    t_account = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    
    #t_username = models.CharField(max_length=30, unique=True, default="")
    #firstname = models.CharField(max_length=20, default="")
    #surname = models.CharField(max_length=20, default="")
    #email = models.EmailField(blank=False, default=None)
    
    g_id = models.ForeignKey(Gym, on_delete=models.CASCADE, default=None)
    contact_no = models.CharField(max_length=14, default=0)
    specialism = models.CharField(max_length=512,default="N/A")
    sex = models.CharField(max_length=16, default="unspecified")
    img = models.ImageField(upload_to='trainerProfile_images',blank=True,default=None)
    price = models.CharField(max_length=10, default="unknown")
    
    def __str__(self):
        return self.t_account.username
    
class Booking(models.Model):
    username = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    t_username = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=datetime.datetime.now())
    location = models.CharField(max_length=30)
    
    @property
    def b_id(self):
        return self.id
    
    def __str__(self):
        return str(self.b_id)

class Trainer_Comment(models.Model):
    username = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    t_username = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    comment = models.CharField(max_length=512)
    datetime = models.DateTimeField(default=datetime.datetime.now())
    
    @property
    def tc_id(self):
        return self.id
        
    def __str__(self):
        return str(self.tc_id)