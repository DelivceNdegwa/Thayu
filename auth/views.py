from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import *

def customer_signup(request):
    message = ""
    
    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST, request.FILES)
        
        if form.is_valid:
            first_name = request.POST.get('first_name')
            last_name =request.POST.get('last_name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password1 = request.POST.get('password1')
            
            if password == password1:
                print(f"FORM_ERRORS: {form.errors}")
                form.save()
                customer_username = first_name+last_name
                User.objects.create_user(
                    username=customer_username,
                    password=password,
                    email=email
                )
                user = authenticate(username=customer_username, password=password)
                
                if user is not None:
                    login(request, user)
                    return redirect(reverse('customer:index'))
                else:
                    message = "Username or password was invalid, try again"
    context = {
        "message": message
    }
    
    return render(request, "authentication/sign_up.html", context)
            
@login_required
def signout(request):
    logout(request)
    
    return redirect(reverse('customer:index'))