from os import name
from django.urls import path
from django.urls.resolvers import URLPattern
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index,name="index"),
    path('register',views.register,name="register"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('user_login',views.user_login,name="user_login"),
    path('Animal',views.Animal,name="Animal"),
    path('user_logout',views.user_logout,name="user_logout"),
    path('user_logout',views.user_logout,name="user_logout"),
    path('user_logout',views.user_logout,name="user_logout"),
    path('view_animal',views.view_animal,name="view_animal"),
    path('add_animal',views.add_animal,name="add_animal"),
    path('animal_update/<int:animal_id>',views.animal_update,name="animal_update"),
    path('animal_delete/<int:animal_id>',views.animal_delete,name="animal_delete"),
    path('view_doctors',views.view_doctors,name='view_doctors'),
    path('review',views.review,name="review"),

    path('add_doctor_details',views.add_doctor_details,name='add_doctor_details'),

    path('delete_doctor/<int:id>',views.delete_doctor,name='delete_doctor'),

    path('view_users',views.view_users,name='view_users'),
    path('delete_user/<int:id>',views.delete_user,name='delete_user'),

    path('add_food_products',views.add_food_products,name='add_food_products'),

    path('view_food_products',views.view_food_products,name='view_food_products'),

    path('update_food_products/<int:id>',views.update_food_products,name='update_food_products'),
    path('delete_food_products/<int:id>',views.delete_food_products,name='delete_food_products'),

    path('add_loan',views.add_loan,name='add_loan'),

    path('view_my_loans',views.view_my_loans,name='view_my_loans'),

    path('view_all_pending_loans',views.view_all_pending_loans,name='view_all_pending_loans'),

    path('update_loan/<int:id>',views.update_loan,name='update_loan'),

    path('add_fertilizer',views.add_fertilizer,name='add_fertilizer'),
    path('view_fertilizer_products',views.view_fertilizer_products,name='view_fertilizer_products'),
    path('update_fertilizer_products/<int:id>',views.update_fertilizer_products,name='update_fertilizer_products'),
    path('delete_fertilizer_products/<int:id>',views.delete_fertilizer_products,name='delete_fertilizer_products'),

    path('add_symptom<int:id>',views.add_symptom,name='add_symptom'),
    path('view_my_symptoms',views.view_my_symptoms,name='view_my_symptoms'),

    path('view_my_work',views.view_my_work,name='view_my_work'),

    path('add_consultation/<int:id>',views.add_consultation,name='add_consultation'),

    path('for_my_consultation',views.for_my_consultation,name='for_my_consultation'),

    path('search',views.search,name='search'),

    path('view_events',views.view_events,name='view_events'),
    path('register_event/<int:id>',views.register_event,name='register_event'),





]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)