from django.urls import path
from vault import views

urlpatterns=[
   path('',views.u_login),
   path('register',views.register),
   path('uvault',views.u_vault),
   path('add_vault',views.vault_add),
    
]