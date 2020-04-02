from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class UserProfile(models.Model):
    account = models.OneToOneField(User, default=None, null=False, on_delete=models.CASCADE)
    #To access username, firstname, lastname, email and password use:
    #account.username
    #account.first_name
    #account.last_name
    #account.email
    #account.password
    
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
    #To access username, firstname, lastname, email and password use:
    #t_account.username
    #t_account.first_name
    #t_account.last_name
    #t_account.email
    #t_account.password
    
    g_id = models.ForeignKey(Gym, on_delete=models.CASCADE, default=None, blank=True, null=False)
    contact_no = models.CharField(max_length=14, default=0)
    specialism = models.CharField(max_length=512,default="N/A")
    sex = models.CharField(max_length=16, default="unspecified")
    img = models.ImageField(upload_to='trainerProfile_images',blank=True,default=None)
    price = models.CharField(max_length=10, default="unknown")
    
    def getGymName(self):
        return self.g_id.name
    
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