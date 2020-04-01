from django.urls import path
from ptfinderApp import views
from django.urls import re_path

app_name = 'ptfinder'

urlpatterns = [
    path('', views.index, name="index"),
    path('user/', views.user, name='user'),
    path('user/login/', views.login , name='login'),
    path('user/register/', views.register , name='register'),
    path('user/register/trainer', views.trainer_register , name='trainer_register'),
    re_path(r'^user/(?P<username>.*)/$', views.user_profile , name='user_profile'),
    re_path(r'^user/(?P<username>.*)/edit_profile/$', views.edit_profile , name='edit_profile'),
    path('trainer/', views.trainer , name='trainer'),
    re_path(r'^trainer/(?P<account>.*)/$', views.trainer_profile , name='trainer_profile'), 
    path('book/', views.book , name='book'),
    re_path(r'^book/(?P<account>.*)/create_booking/$', views.create_booking, name='create_booking'),
    re_path(r'^book/(?P<username>.*)/$', views.view_bookings , name='view_bookings'),
    re_path(r'^book/(?P<account>.*)/$', views.view_bookings , name='view_bookings'),
    path('contact_us/', views.contact_us , name='contact_us'),
    path('gym/', views.gym , name='gym'), 
    re_path(r'^gym/(?P<name>.*)/$', views.gym_profile , name='gym_profile'), 
]
