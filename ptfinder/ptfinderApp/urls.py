from django.urls import path
from ptfinderApp import views

app_name = 'ptfinder'

urlpatterns = [
    path('', views.index, name="index"),
    path('user/', views.user, name='user'),
    path('user/login/', views.login , name='login'),
    path('user/register/trainer', views.trainer_register , name='trainer_register'),
    path('user/register/', views.register , name='register'),
    path('user/<str:username>/', views.user_profile , name='user_profile'),
    path('user/<str:username>/edit_profile/', views.edit_profile , name='edit_profile'),
    path('trainer/', views.trainer , name='trainer'),
    path('trainer/<str:t_username>/', views.trainer_profile , name='trainer_profile'), 
    path('book/', views.book , name='book'),
    path('book/create_booking/', views.create_booking, name='create_booking'),
    path('book/<str:username>/', views.view_bookings , name='view_bookings'),
    path('book/<str:t_username>/', views.view_bookings , name='view_bookings'),
    path('contact_us/', views.contact_us , name='contact_us'),
    path('gym/', views.gym , name='gym'), 
    path('gym/<int:g_id>/', views.gym_profile , name='gym_profile'), 
]
