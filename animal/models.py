
from django.contrib.auth.models import User
from django.db import models
from django.db.models.base import Model
from django.core.exceptions import ValidationError
from django.db.models.deletion import CASCADE
from django.db.models.expressions import F
from django.db.models.fields import CharField
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
import time
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField




# Create your models here.
class Register(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    phone=PhoneNumberField(null=True,blank=True)
    address=models.TextField()
    def __str__(self):
        return str(self.user.username)

class AnimalType(models.Model):
    name=CharField(max_length=40)
    def __str__(self):
        return str(self.name)


class Animal(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=40)
    color=models.CharField(max_length=30)
    male='male'
    female='female'
    sex_types=[
        (male,'male'),
        (female,'female')
    ]
    sex=models.CharField(max_length=30,choices=sex_types,default=male)
    year=models.IntegerField()
    month=models.IntegerField()
    date=models.DateTimeField(default=timezone.now)
    photo=models.ImageField(upload_to='images',null=True,blank=True)
    pet='pet'
    farm='farm'
    types=[
        (pet,'pet'),
        (farm,'farm')
    ]
    animal_type=models.CharField(max_length=50,choices=types,null=True,blank=True,default=pet)
    place=models.CharField(max_length=50)
    description=models.TextField()
    price=models.IntegerField()
    paid=models.BooleanField(default=False)
    def __str__(self):
        return str(self.user.username)



class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    certificate=models.FileField(upload_to='files',null=True,blank=True)
    license=models.CharField(max_length=50,null=True,blank=True)
    phone=models.IntegerField()
    date=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.name)



class Review(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    content=models.TextField()
    date=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.user.username)




class FoodProducts(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    food_name=models.CharField(max_length=50)
    quantity=models.IntegerField()
    description=models.TextField()
    place=models.CharField(max_length=50,null=True,blank=True)
    amount=models.IntegerField()
    available=models.BooleanField(default=True)
    def __str__(self):
        return str(self.food_name)


class LoanType(models.Model):
    loan_name=models.CharField(max_length=50)
    def __str__(self):
        return str(self.loan_name)



class Loan(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    email=models.CharField(max_length=50)
    loan_type=models.ForeignKey(LoanType,on_delete=models.CASCADE,null=True,blank=True)
    amount=models.IntegerField()
    bank_name=models.CharField(max_length=50)
    approved='approved'
    pending='pending'
    rejected='rejected'

    statuses=[
        (approved,'approved'),
        (pending,'pending'),
        (rejected,'rejected')
    ]
    status=models.CharField(max_length=30,choices=statuses,default=pending)

    def __str__(self):
        return str(self.user.username)



class Symptoms(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE,null=True,blank=True)
    video=models.FileField(upload_to='videos',null=True,blank=True)
    description=models.TextField()
    animal_name=models.CharField(max_length=50)
    pet='pet'
    farm='farm'
    types=[
        (pet,'pet'),
        (farm,'farm')
    ]
    animal_type=models.CharField(max_length=50,choices=types,null=True,blank=True,default=pet)
    
    def __str__(self):
        return str(self.user.username)



class Fertilizer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    fertilizer_name=models.CharField(max_length=50)
    quantity=models.IntegerField()
    description=models.TextField()
    place=models.CharField(max_length=50,null=True,blank=True)
    amount=models.IntegerField()
    available=models.BooleanField(default=True)
    def __str__(self):
        return str(self.fertilizer_name)



class Consultation(models.Model):
    symptom=models.ForeignKey(Symptoms,on_delete=models.CASCADE,null=True,blank=True)
    description=models.TextField()
    amount=models.IntegerField()
    def __str__(self):
        return str(self.symptom.user.username)





class BuyFood(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    food=models.ForeignKey(FoodProducts,on_delete=models.CASCADE,null=True,blank=True)
    paid=models.BooleanField(default=False)
    def __str__(self):
        return str(self.user.username)





class Event(models.Model):
    event_name=models.CharField(max_length=50)
    event_date=models.DateField()
    event_area=models.CharField(max_length=50)
    event_time=models.CharField(max_length=30)
    description=models.TextField()
    fee=models.IntegerField()
    date=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.event_name)



class EventRegister(models.Model):
    event=models.ForeignKey(Event,on_delete=models.CASCADE,null=True,blank=True)
    user=models.ForeignKey(Register,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return str(self.user.user.username)