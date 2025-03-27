from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.contrib.auth.forms import UserCreationForm#!create new user
from django.contrib.auth import login as auth_log,authenticate,logout as auth_logout,login as auth_login
#!from django.contrib.auth import login=> for make login to user when signup 
from . form import signupform
from django.contrib.auth.decorators import login_required
from boards.models import *
# Create your views here.

def signup(request):
    form=signupform()
    if request.method=='POST':
        form=signupform(request.POST)
        if form.is_valid():
            user=form.save()
            auth_log(request,user)
            return redirect('home')
    return render(request,'accounts/signup.html',{'form':form})




def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)  
        
        if user is not None:
            auth_login(request, user) 
            return redirect("home")  
        
        else:
            return render(request, "accounts/login.html", {"error": "Invalid username or password"})

    return render(request, "accounts/login.html")

            
        
@login_required
def update_account(request):
    user = request.user
    if request.method == "POST":
        username = request.POST.get('username')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        if username:
            user.username = username
        if last_name:
            user.last_name = last_name
        if email:
            user.email = email

        user.save()
        return redirect('home')

    return render(request,'accounts/updat_account.html')

        





























# def login_views(request):
#     if request.method=='POST':
#         password=request.POST.get('pass')
#         username=request.POST.get('username')
#         user=authenticate(
#             password=password,
#             username=username
#         )
#         if user is not None:
#             auth_log(request,user)
#             return redirect ('test')
#         else:
#             return render(request,'accounts/login.html')
        
#     else:
#         return render(request,'accounts/login.html')

# def logout_views(request):
#     auth_logout(request)
#     return HttpResponse ('login')
# @login_required(login_url='/signup/')
# def test(request):
#     user=request.user
#     return render(request,'accounts/test.html',{'user':user})