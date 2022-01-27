from django import forms
from django.db.models import fields
from . models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import DateInput, Select, Textarea, TextInput
from django.utils.translation import ugettext_lazy as _
from animal.models import Animal

class UserForm(UserCreationForm):
    username=forms.CharField(help_text=None,label='username')
    password1=forms.CharField(help_text=None,widget=forms.PasswordInput,label='Password')
    password2=forms.CharField(help_text=None,widget=forms.PasswordInput,label='Confirm Password')
    class Meta:
        model=User
        fields=('username','password1','password2','first_name','last_name','email')
        labels=('password1','Password','password2','Confirm password')

class ProfileForm(forms.ModelForm):
    address=forms.Textarea()
    class Meta:
        model=Register
        fields=('address','phone')


class AddAnimalForm(forms.ModelForm):
    description=forms.Textarea()
    class Meta:
        model=Animal
        fields=('name','color','sex','year','month','photo','place','animal_type','description','price')


class ReviewForm(forms.ModelForm):
    content=forms.Textarea()
    class Meta:
        model=Review
        fields=('content',)



class DoctorForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields=('name','place','license','certificate','phone')



class FoodProductForm(forms.ModelForm):
    class Meta:
        model=FoodProducts
        fields=('food_name','quantity','description','place','amount')




class LoanForm(forms.ModelForm):
    class Meta:
        model=Loan
        fields=('email','loan_type','amount','bank_name',)


class UpdateLoanForm(forms.ModelForm):
    class Meta:
        model=Loan
        fields=('status',)



class FertilizerForm(forms.ModelForm):
    class Meta:
        model=Fertilizer
        fields=('fertilizer_name','quantity','description','place','amount')


class EventForm(forms.ModelForm):
    class Meta:
        model=Event
        fields=('event_name','event_date','event_area','event_time','description','fee')


class SymptomForm(forms.ModelForm):
    class Meta:
        model=Symptoms
        fields=('video','description','animal_name','animal_type')



class ConsultationForm(forms.ModelForm):
    class Meta:
        model=Consultation
        fields=('description','amount')
