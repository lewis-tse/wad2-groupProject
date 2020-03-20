from django.contrib import admin
from ptfinderApp.models import UserProfile, Gym, Trainer, Booking, Trainer_Comment
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Gym)
admin.site.register(Trainer)
admin.site.register(Booking)
admin.site.register(Trainer_Comment)