from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User

# Create your views here.
def u_login(req):
    if 'vault' in req.session:
        return redirect(u_vault)
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['password']
        vault=authenticate(username=uname,password=password)
        if vault:
            login(req,vault)
        else:
            messages.warning(req,'Invalid user name or password')
            return redirect(u_login)
        return redirect(u_vault)
    else:
        return render(req,'login.html')
    
def u_logout(req):
    logout(req)
    req.session.flush()
    return redirect(u_login)
    

def register(req):
    if req.method=='POST':
        uname=req.POST['uname']
        email=req.POST['email']
        pswd=req.POST['password']
        try:
            data=User.objects.create_user(first_name=uname,email=email,username=email,password=pswd)
            data.save()
            return redirect(u_login)
        except:
            messages.warning(req,'Email Already Exit')
            return redirect(register)
    else:
        return render(req,'user/register.html')
def u_vault(req):
    data=File.objects.filter(user=req.user)
    return render(req,'user/vault.html',{'data':data})

def add_vault(req,id):
    if req.method=='POST':
        user=User.objects.get(pk=id)
        name=req.POST['name']
        files=req.FILES['files']
        data=File.objects.create(user=user,name=name,files=files)
        data.save()
        return redirect(u_vault)
    else:
        
        return render(req,'user/add_vault.html')
def delete(req,id):
    data=File.objects.get(pk=id)
    data.delete()
    return redirect(u_vault)

