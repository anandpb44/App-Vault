from django.urls import path
from vault import views

urlpatterns=[
   path('',views.u_login),
   path('logout',views.u_logout),
   path('register',views.register),
   path('uvault',views.u_vault),
   path('add/<id>',views.add_vault),
    
]