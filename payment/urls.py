from django.urls import path
from .import views

app_name = 'payment'
urlpatterns = [
    path('payment/<int:animal_id>',views.payment,name='payment'),
    path('payment2/<int:id>',views.payment2,name='payment2'),
    path('payment-status', views.payment_status, name='payment-status'),

    path('view_payment',views.view_payment,name='view_payment'),


 
    
]
