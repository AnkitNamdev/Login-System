from django.shortcuts import render
from . forms import Registration,LoginForm

def sign_up(req):
    if req.method=="POST":
        fm=Registration(req.POST)
        if fm.is_valid():
            fm.save()
    fm=Registration()
    return render(req,'login1/signup.html',{'fm':fm})

def log_in(req):
    if req.method=="POST":
        pass

    else:
        fm=LoginForm()
        return render(req,"login1/login.html",{'fm':fm})


