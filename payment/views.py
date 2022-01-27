
from .models import *
from django.shortcuts import render
import razorpay
from .forms import PaymentForm
from animal.models import *

def payment(request,animal_id):
    animal=Animal.objects.get(id=animal_id)
    amount=animal.price
    if request.method == "POST":
        animal=Animal.objects.get(id=animal_id)
        amount=animal.price
        name = request.user
        amount1=amount
        animal_name=animal.name
        amount = int(amount1) *100
        client = razorpay.Client(auth=('rzp_test_48Z9LMTDVAN5JU', 'gMxfhwgZ73ANYJQCeblLMy7W'))
        response_payment = client.order.create(dict(amount=amount,
                                                    currency='INR')
                                               )

        order_id = response_payment['id']
        order_status = response_payment['status']
        
        if order_status == 'created':
            payment = Payment(
                user=request.user,
                name=name,
                amount=amount1,
                order_id=order_id,
                animal_name=animal_name,
               
            )
          
        payment.save()
        animal=Animal.objects.update_or_create(id=animal_id,
        defaults={'paid':True}
        )
        
        response_payment['name'] = name

        form = PaymentForm(request.POST or None)
        return render(request, 'payment/payment.html', {'form':form,'payment': response_payment,'amount':amount1})

    form = PaymentForm()
    return render(request, 'payment/payment.html', {'form': form,'amount':amount})






def payment2(request,id):
    try:
        animal=FoodProducts.objects.get(id=id)
    except:
        pass
    try:
        animal=Fertilizer.objects.get(id=id)
    except:
        pass
    try:
        animal=Consultation.objects.get(id=id)
    except:
        pass


    amount=animal.amount
    if request.method == "POST":
        try:
            animal=FoodProducts.objects.get(id=id)
        except:
            pass
        try:
            animal=Fertilizer.objects.get(id=id)
        except:
            pass
        try:
            animal=Consultation.objects.get(id=id)
        except:
            pass
        amount=animal.amount
        name = request.user
        amount1=amount
        
        amount = int(amount1) *100
        client = razorpay.Client(auth=('rzp_test_48Z9LMTDVAN5JU', 'gMxfhwgZ73ANYJQCeblLMy7W'))
        response_payment = client.order.create(dict(amount=amount,
                                                    currency='INR')
                                               )

        order_id = response_payment['id']
        order_status = response_payment['status']
        
        if order_status == 'created':
            payment = Payment(
                user=request.user,
                name=name,
                amount=amount1,
                order_id=order_id,
                
               
            )

          
        payment.save()
        try:
            buy_products=BuyFood(
                user=request.user,
                food=animal,
                paid=True
            )
            buy_products.save()
        except:
            pass
        
        
        response_payment['name'] = name

        form = PaymentForm(request.POST or None)
        return render(request, 'payment/payment2.html', {'form':form,'payment': response_payment,'amount':amount1})

    form = PaymentForm()
    return render(request, 'payment/payment2.html', {'form': form,'amount':amount})


def payment_status(request):
    response = request.POST
    params_dict = {

       'razorpay_order_id': response['razorpay_order_id'],
       'razorpay_payment_id': response['razorpay_payment_id'],
       'razorpay_signature': response['razorpay_signature'],
     
    }

    # client instance
    client = razorpay.Client(auth=('rzp_test_48Z9LMTDVAN5JU', 'gMxfhwgZ73ANYJQCeblLMy7W'))
    

    try:
        status = client.utility.verify_payment_signature(params_dict)
        payment = Payment.objects.get(order_id=response['razorpay_order_id'])
        payment.payment_id = response['razorpay_payment_id']
        payment.user=request.user
        payment.is_paid = True
        payment.save()

       
        
        return render(request, 'payment/payment_status.html', {'status': True,'payment_id':payment.payment_id})
    except:
        return render(request, 'payment/payment_status.html', {'status': False})






def view_payment(request):
    payments=Payment.objects.filter(is_paid=True).order_by('-id')
    return render(request,'view_payment.html',{'payments':payments})
