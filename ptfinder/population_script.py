#populate_ptfinder.py
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ptfinder.settings')

import django
django.setup()
from django.core.files import File
from django.contrib.auth.models import User
from ptfinderApp.models import UserProfile, Gym, Trainer, Trainer_Comment, Booking

import datetime
import urllib.request

def populate():
    users = [
            {'username':'user1', 'first_name':'Charley', 'last_name':'Hopkins', 'email':'CHopkins1@gmail.com', 'password':'user1password',
                'experience':'None', 'sex':'Male', 'location':'Aberdeen', 'img':'Charley.jpg'},
            {'username':'user2', 'first_name':'Rachael', 'last_name':'Boyd', 'email':'RBoyd2@gmail.com', 'password':'user2password',
                'experience':'3 Years', 'sex':'Female', 'location':'Stirling', 'img':'Rachael.jpg'},
            {'username':'user3', 'first_name':'Isla', 'last_name':'Smart', 'email':'ISmart3@gmail.com', 'password':'user3password',
                'experience':'None', 'sex':'Female', 'location':'Glasgow', 'img':'Isla.jpg'},
            {'username':'user4', 'first_name':'Matias', 'last_name':'Sharp', 'email':'MSharp4@gmail.com', 'password':'user4password',
                'experience':'1 Year', 'sex':'Male', 'location':'Aberdeen', 'img':'Matias.jpg'},
            {'username':'user5', 'first_name':'Anita', 'last_name':'Ross', 'email':'ARoss5@gmail.com', 'password':'user5password',
                'experience':'2 Years', 'sex':'Female', 'location':'Glasgow', 'img':'Anita.jpg'}]
    
    gyms = [
            {'name':'Self Employed', 'owner':'Self Employed', 'address_line1':'N/A', 'address_line2':'N/A', 'address_postcode':'N/A', 'city':'N/A', 'img':'Self_employed.jpg', 'description':'This trainer is not affiliated with a gym'},
            {'name':'Gyms 4 U', 'owner':'Katie Johnson', 'address_line1':'212 Sturgeon Street', 'address_line2':'N/A', 'address_postcode':'S06 7LG', 'city':'Stirling', 'img':'Gyms_4_u.jpg', 'description':'Cheap and affordable'},
            {'name':'Fitness Planet', 'owner':'Phil Zubert', 'address_line1':'31 Burton Road', 'address_line2':'N/A', 'address_postcode':'G19 9PE', 'city':'Glasgow', 'img':'Fitness_planet.jpg', 'description':'A wide range of classes and equipment'},
            {'name':'Revolve', 'owner':'Maria Plum', 'address_line1':'467 Granite Avenue', 'address_line2':'N/A', 'address_postcode':'AB6 4RT', 'city':'Aberdeen', 'img':'Revolve.jpg', 'description':'Cylce based exercise'},
            {'name':'Weight Shedderz', 'owner':'Calum Farmer', 'address_line1':'24 Burrow Street', 'address_line2':'N/A', 'address_postcode':'G01 5FB', 'city':'Glasgow', 'img':'Weight_shedderz.jpg', 'description':'Hardcore exercise to cut those unwanted kilograms'},]
    
    trainers = [
                {'username':'trainer1', 'first_name':'Max', 'last_name':'Morin', 'email':'MMorin1@gmail.com', 'password':'trainer1password',
                'g_id':1, 'contact_no':'555 432 236', 'specialism':'Cardio', 'sex':'Male','location':'Aberdeen', 'img':'Max.jpg', 'price':'£10/hr'},
                {'username':'trainer2', 'first_name':'Caden', 'last_name':'Lee', 'email':'CLee2@gmail.com', 'password':'trainer2password',
                'g_id':3, 'contact_no':'573 876 992', 'specialism':'Free Weights', 'sex':'Male','location':'Stirling', 'img':'Caden.jpg', 'price':'£30/hr'},
                {'username':'trainer3', 'first_name':'Storm', 'last_name':'Leonard', 'email':'SLeonard3@gmail.com', 'password':'trainer3password',
                'g_id':4, 'contact_no':'233 111 786', 'specialism':'Upper Body', 'sex':'Female','location':'Glasgow', 'img':'Storm.jpg', 'price':'£15/hr'},
                {'username':'trainer4', 'first_name':'Sarah', 'last_name':'Marquez', 'email':'SMarquez4@gmail.com', 'password':'trainer4password',
                'g_id':5, 'contact_no':'286 667 987', 'specialism':'Agility', 'sex':'Female','location':'Glasgow', 'img':'Sarah.jpg', 'price':'£20/hr'},
                {'username':'trainer5', 'first_name':'Joan', 'last_name':'Stanley', 'email':'JStanley5@gmail.com', 'password':'trainer5passord',
                'g_id':1, 'contact_no':'647 558 900', 'specialism':'Cardio', 'sex':'Female','location':'Aberdeen', 'img':'Joan.jpg', 'price':'£20/hr'}]
    
    comments = [
                {'username':'user1','t_username':'trainer2','comment':'Had a blast','datetime':datetime.datetime.now()},
                {'username':'user5','t_username':'trainer3','comment':'Great trainer but too intense for me!','datetime':datetime.datetime.now()},
                {'username':'user1','t_username':'trainer1','comment':'Really friendly, cant wait to book again','datetime':datetime.datetime.now()},
                {'username':'user2','t_username':'trainer3','comment':'Helped me push my limits','datetime':datetime.datetime.now()},
                {'username':'user4','t_username':'trainer5','comment':'Horrible, turned up late and was really rude!','datetime':datetime.datetime.now()}]
    
    bookings = [
                {'username':'user3','t_username':'trainer4','datetime':datetime.datetime.now(),'location':'Glasgow'},
                {'username':'user4','t_username':'trainer2','datetime':datetime.datetime.now(),'location':'Stirling'},
                {'username':'user2','t_username':'trainer5','datetime':datetime.datetime.now(),'location':'Aberdeen'},
                {'username':'user4','t_username':'trainer1','datetime':datetime.datetime.now(),'location':'Aberdeen'},
                {'username':'user1','t_username':'trainer4','datetime':datetime.datetime.now(),'location':'Glasgow'}]
    
    counter = 1
    for gym in gyms:
        g = add_gym(gym,counter)
        counter += 1
        
    for user in users:
        u = add_user(user)
        
    for trainer in trainers:
        t = add_trainer(trainer)
    
    counter = 1
    for booking in bookings:
        b = add_booking(booking, counter)
        counter += 1
    
    counter = 1
    for comment in comments:
        c = add_comment(comment, counter)
        counter += 1
        
def add_user(user):
    u = User.objects.get_or_create(username=user['username'])[0]
    up = UserProfile.objects.get_or_create(account = u)[0]
    #assign attributes
    u.first_name = user['first_name']
    u.last_name = user['last_name']
    u.email = user['email']
    u.password = user['password']
    up.experience = user['experience']
    up.sex = user['sex']
    up.location = user['location']
    
    FILE_PATH = os.getcwd()
    up.img.save(user['first_name']+".jpg", File(open(FILE_PATH+"\\population_imgs\\"+user['img'], 'rb')))
    
    u.save()
    up.save()
    return up
    
def add_gym(gym, counter):
    g = Gym.objects.get_or_create(id=counter)[0]
    #assign attributes
    g.name = gym['name']
    g.owner = gym['owner']
    g.address_line1 = gym['address_line1']
    g.address_line2 = gym['address_line2']
    g.address_postcode = gym['address_postcode']
    g.city = gym['city']
    
    FILE_PATH = os.getcwd()
    g.images.save(gym['name']+".jpg", File(open(FILE_PATH+"\\population_imgs\\"+gym['img'], 'rb')))
    
    g.description = gym['description']
    
    g.save()
    return g

def add_trainer(trainer):
    t = User.objects.get_or_create(username=trainer['username'])[0]
    tp = Trainer.objects.get_or_create(t_account = t,g_id = Gym.objects.get(id=trainer['g_id']))[0]
    #assign attributes
    t.first_name = trainer['first_name']
    t.last_name = trainer['last_name']
    t.email = trainer['email']
    t.password = trainer['password']
    #tp.g_id = Gym.objects.get(id=trainer['g_id'])
    tp.contact_no = trainer['contact_no']
    tp.specialism = trainer['specialism']
    tp.sex = trainer['sex']
    
    FILE_PATH = os.getcwd()
    tp.img.save(trainer['first_name']+".jpg", File(open(FILE_PATH+"\\population_imgs\\"+trainer['img'], 'rb')))
    
    tp.price = trainer['price']
    
    t.save()
    tp.save()
    return tp

def add_comment(comment, counter):
    user = User.objects.get(username=comment['username'])
    tuser = User.objects.get(username=comment['t_username'])
    c = Trainer_Comment.objects.get_or_create(id=counter, username=UserProfile.objects.get(account=user),t_username=Trainer.objects.get(t_account=tuser))[0]
    #assign attributes
    #c.username = comment['username']
    #c.t_username = comment['t_username']
    c.comment = comment['comment']
    c.datetime = comment['datetime']
    
    c.save()
    return c

def add_booking(booking, counter):
    user = User.objects.get(username=booking['username'])
    tuser = User.objects.get(username=booking['t_username'])
    b = Booking.objects.get_or_create(id=counter, username=UserProfile.objects.get(account=user),trainer_username=Trainer.objects.get(t_account=tuser))[0]
    #assign attributes
    #b.username = booking['username']
    #b.t_username = booking['t_username']
    b.datetime = booking['datetime']
    b.location = booking['location']
    
    b.save()
    return b

if __name__ == '__main__':
    print('populating PTFinder database...')
    populate()
    print('population complete.')