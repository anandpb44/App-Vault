from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def login(req):
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['password']
        vault=authenticate(username=uname,password=password)
        if vault:
            login(req)
            return redirect(u_vault)
    else:
        
        return render(req,'login.html')
    

def register(req):
    if req.method=='POST':
        uname=req.POST['uname']
        email=req.POST['email']
        pswd=req.POST['password']
        try:
            data=User.objects.create_user(first_name=uname,email=email,username=email,password=pswd)
            data.save()
            return redirect(login)
        except:
            messages.warning(req,'Email Already Exit')
            return redirect(register)
    else:
        return render(req,'user/register.html')
def u_vault(req):
    return render(req,'user/vault.html')


