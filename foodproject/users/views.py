from django.shortcuts import render,redirect
from django.contrib import messages
from django.urls import reverse
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required

def registerview(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username}!!! You are currently logged in')
            return redirect(reverse('login'))
    else:
        form = RegisterForm()
    return render(request,'register.html',{"form":form})

@login_required
def profile(request):
    return render(request,'profile.html')
