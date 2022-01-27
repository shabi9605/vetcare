from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from . models import *
from . forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request,'index.html')


def register(request):
    reg=False
    
    if request.method=="POST":
        user_form=UserForm(data=request.POST)
        profile_form=ProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.save()
            profile=profile_form.save(commit=False)
            profile.user=user
            profile.save()
            reg=True
        else:
            HttpResponse("invalid form")      
    else:
        user_form=UserForm()
        profile_form=ProfileForm() 
    return render(request,'register.html',{'register':reg,'user_form':user_form,'profile_form':profile_form})


def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('dashboard'))
            else:
                return HttpResponse("not active")
        else:
            return HttpResponse("invalid username or password")
    else:
        return render(request,'login.html')

def dashboard(request):
    return render(request,'dashboard.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')


def view_animal(request):
    animal=Animal.objects.all()
    return render(request,'view_animal.html',{'animal':animal})


def add_animal(request):
    myselling=Animal.objects.filter(user=request.user)
    if request.method=="POST":
        add_animal_form=AddAnimalForm(request.POST,request.FILES)
        if add_animal_form.is_valid():
            cp=Animal(user=request.user,name=add_animal_form.cleaned_data['name'],color=add_animal_form.cleaned_data['color'],sex=add_animal_form.cleaned_data['sex'],birth_date=add_animal_form.cleaned_data['birth_date'],photo=add_animal_form.cleaned_data['photo'],animal_type=add_animal_form.cleaned_data['animal_type'],description=add_animal_form.cleaned_data['description'],price=add_animal_form.cleaned_data['price'])
            cp.save()

            
            return redirect('add_animal')
        else:
            return HttpResponse("Invalid form")
    add_animal_form=AddAnimalForm()
    return render(request,'add_animal.html',{'form':add_animal_form,'myselling':myselling})


def animal_update(request,animal_id):
    animal_update=Animal.objects.get(id=animal_id)
    print(animal_update)
    update_animal_form=AddAnimalForm(instance=animal_update)
    if request.method=="POST":
        update_requirement_form=AddAnimalForm(request.POST,request.FILES,instance=animal_update)
        update_requirement_form.save()
        return redirect('dashboard')
    return render(request,'update_animal.html',{'update_animal_form':update_animal_form})


def animal_delete(request,animal_id):
    deleteitem=Animal.objects.get(id=animal_id)
    deleteitem.delete()
    return redirect('dashboard')


def view_doctors(request):
    doctors=Doctor.objects.all()
    return render(request,'view_doctors.html',{'doctors':doctors})



def review(request):
    review=Review.objects.filter(user=request.user)
    
    if request.method=="POST":
        review_form=ReviewForm(request.POST)
        if review_form.is_valid():
            cp=Review(user=request.user,content=review_form.cleaned_data['content'])
            cp.save()

            
            return redirect('review')
        else:
            return HttpResponse("Invalid form")
    review_form=ReviewForm()
    return render(request,'review.html',{'review_form':review_form,'review':review})









def add_doctor_details(request):
    if request.method=="POST":
        form1=UserForm(request.POST)
        doctor_form=DoctorForm(request.POST,request.FILES)
        if doctor_form.is_valid():
            form1.save()
            doctor_form.save()

            
            return redirect('view_doctors')
        else:
            return HttpResponse("Invalid form")
    doctor_form=DoctorForm()
    form1=UserForm()
    return render(request,'add_doctor.html',{'doctor_form':doctor_form,'form1':form1})



def delete_doctor(request,id):
    doctor=Doctor.objects.get(id=id)
    doctor.delete()
    return redirect('view_doctors')



def view_users(request):
    users=Register.objects.all().order_by('-id')
    return render(request,'view_users.html',{'users':users})


def delete_user(request,id):
    user=Register.objects.get(id=id)
    user.delete()
    return redirect('view_users')



def add_food_products(request):
    if request.method=="POST":
        food_form=FoodProductForm(request.POST,request.FILES)
        if food_form.is_valid():
            cp=FoodProducts(user=request.user,fertilizer_name=food_form.cleaned_data['fertilizer_name'],
            quantity=food_form.cleaned_data['quantity'],description=food_form.cleaned_data['description'],
            place=food_form.cleaned_data['place'],amount=food_form.cleaned_data['amount'])
            cp.save()

            
            return redirect('view_food_products')
        else:
            return HttpResponse("Invalid form")
    food_form=FoodProductForm()
    return render(request,'add_food_products.html',{'form':food_form})



def view_food_products(request):
    food_products=FoodProducts.objects.all().order_by('-id')
    return render(request,'view_food_products.html',{'food_products':food_products})



def update_food_products(request,id):
    food_update=FoodProducts.objects.get(id=id)
    print(food_update)
    update_food_form=FoodProductForm(instance=food_update)
    if request.method=="POST":
        update_food_form=FoodProductForm(request.POST,request.FILES,instance=food_update)
        update_food_form.save()
        return redirect('view_food_products')
    return render(request,'add_food_products.html',{'form':update_food_form})


def delete_food_products(request,id):
    food=FoodProducts.objects.get(id=id)
    food.delete()
    return redirect('view_food_products')




def add_loan(request):
    if request.method=="POST":
        food_form=LoanForm(request.POST,request.FILES)
        if food_form.is_valid():
            cp=Loan(user=request.user,email=food_form.cleaned_data['email'],loan_type=food_form.cleaned_data['loan_type'],
            amount=food_form.cleaned_data['amount'],bank_name=food_form.cleaned_data['bank_name'])
            
            cp.save()

            
            return redirect('view_my_loans')
        else:
            return HttpResponse("Invalid form")
    food_form=LoanForm()
    return render(request,'apply_loan.html',{'form':food_form})



def view_my_loans(request):
    loans=Loan.objects.all()
    return render(request,'view_my_loans.html',{'loans':loans})




def view_all_pending_loans(request):
    loans=Loan.objects.all()
    return render(request,'view_my_loans.html',{'loans':loans})


def update_loan(request,id):
    update=Loan.objects.get(id=id)
    print(update)
    update_loan_form=UpdateLoanForm(instance=update)
    if request.method=="POST":
        update_loan_form=UpdateLoanForm(request.POST,request.FILES,instance=update)
        update_loan_form.save()
        return redirect('view_all_pending_loans')
    return render(request,'apply_loan.html',{'form':update_loan_form})


def add_fertilizer(request):
    if request.method=="POST":
        food_form=FertilizerForm(request.POST,request.FILES)
        if food_form.is_valid():
            cp=Fertilizer(user=request.user,fertilizer_name=food_form.cleaned_data['fertilizer_name'],
            quantity=food_form.cleaned_data['quantity'],description=food_form.cleaned_data['description'],
            place=food_form.cleaned_data['place'],amount=food_form.cleaned_data['amount'])
            cp.save()

            
            return redirect('view_fertilizer_products')
        else:
            return HttpResponse("Invalid form")
    food_form=FertilizerForm()
    return render(request,'add_fertilizer_products.html',{'form':food_form})



def view_fertilizer_products(request):
    food_products=Fertilizer.objects.all().order_by('-id')
    return render(request,'view_fertilizer_products.html',{'food_products':food_products})



def update_fertilizer_products(request,id):
    food_update=Fertilizer.objects.get(id=id)
    print(food_update)
    update_food_form=FoodProductForm(instance=food_update)
    if request.method=="POST":
        update_food_form=FoodProductForm(request.POST,request.FILES,instance=food_update)
        update_food_form.save()
        return redirect('view_fertilizer_products')
    return render(request,'add_food_products.html',{'form':update_food_form})


def delete_fertilizer_products(request,id):
    food=Fertilizer.objects.get(id=id)
    food.delete()
    return redirect('view_food_products')



def add_symptom(request,id):
    if request.method=="POST":
        doctor=Doctor.objects.get(id=id)
        food_form=SymptomForm(request.POST,request.FILES)
        if food_form.is_valid():
            cp=Symptoms(user=request.user,doctor=doctor,video=food_form.cleaned_data['video'],
            description=food_form.cleaned_data['description'],animal_name=food_form.cleaned_data['animal_name'],
            animal_type=food_form.cleaned_data['animal_type'])
            
            cp.save()

            
            return redirect('view_my_symptoms')
        else:
            return HttpResponse("Invalid form")
    food_form=SymptomForm()
    return render(request,'add_symptom.html',{'form':food_form})



def view_my_symptoms(request):
    symptom=Symptoms.objects.filter(user=request.user)
    print(symptom)
    return render(request,'my_symptom.html',{'symptom':symptom})



def view_my_work(request):
    symptom=Symptoms.objects.filter(doctor=request.user.doctor)
    print(symptom)
    return render(request,'my_work.html',{'symptom':symptom})



def add_consultation(request,id):
    symptom=Symptoms.objects.get(id=id)
    if request.method=="POST":
        food_form=ConsultationForm(request.POST,request.FILES)
        if food_form.is_valid():
            cp=Consultation(symptom=symptom,description=food_form.cleaned_data['description'],amount=food_form.cleaned_data['amount'])
            cp.save()

            
            return redirect('view_my_work')
        else:
            return HttpResponse("Invalid form")
    food_form=ConsultationForm()
    return render(request,'add_consultation.html',{'form':food_form})



def for_my_consultation(request):
    consultation=Consultation.objects.filter(symptom__user=request.user)
    print(consultation)
    return render(request,'for_my_consultation.html',{'consultation':consultation})




def search(request):
    if request.method=="GET":
       
        location=request.GET.get('location')
        print(location)
        
        try:
            
            
            animal=Animal.objects.filter(place__icontains=location)
            print(animal)
            food=FoodProducts.objects.filter(place__icontains=location)
            print(food)
            fertilizer=Fertilizer.objects.filter(place__icontains=location)
            print(fertilizer)

            return render(request,'search.html',{'food':food,'fertilizer':fertilizer,'animal':animal})
        except:
            return render(request,'search.html')

        
        
    return render(request,'search.html')



def view_events(request):
    events=Event.objects.all()
    return render(request,'events.html',{'events':events})



def register_event(request,id):
    event=Event.objects.get(id=id)
    cp=EventRegister.objects.create(user=request.user.register,event=event)

    return redirect('dashboard')
     