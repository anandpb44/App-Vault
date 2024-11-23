from django.urls import path
from vault import views

urlpatterns=[
   path('',views.login),
   path('register',views.register),
   path('uvault',views.u_vault),
    
]