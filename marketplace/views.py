from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect

from marketplace.forms import BuyerForm


# Create your views here.

def index(request):
    return render(request, 'Modified_files/home.html')

def signup(request):
    if request.method == 'POST':
        form = BuyerForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data.get('password1'))
            user.is_buyer = True
            user.save()
            return redirect('index')
    else:
        form = BuyerForm()
    return render(request,'Modified_files/sign_up.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('admin_dashboard')
            elif user.is_buyer:
                return  redirect('buyer_dashboard')
        else:
            messages.info(request,'Wrong Email/Password')
    return render(request, 'Modified_files/login.html')

@login_required(login_url='login_view')
def logout_view(request):
    logout(request)
    return redirect('login_view')



