from django.contrib import admin
from .models import*
from django.contrib.admin.decorators import register
# Register your models here.
admin.site.register(Register)
admin.site.register(AnimalType)
admin.site.register(Animal)
admin.site.register(Doctor)
admin.site.register(Review)
admin.site.register(FoodProducts)
admin.site.register(LoanType)
admin.site.register(Loan)
admin.site.register(Symptoms)
admin.site.register(Fertilizer)
admin.site.register(Consultation)
admin.site.register(Event)
admin.site.register(EventRegister)

