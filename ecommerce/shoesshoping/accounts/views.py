from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# Create your views here.


def login_view(request):   
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = email)
        if not user_obj.exists():
            messages.warning(request, 'account not found')
            return HttpResponseRedirect(request.path_info)
        
        if not user_obj[0].is_email_verified:
            messages.warning(request, 'your account is not verified')
            return HttpResponseRedirect(request.path_info)
        
        user_obj = authenticate(username = email, password = password)
        if user_obj:
            login(request, user_obj)
            return redirect('/')
        
        messages.warning(request, 'invalid credentials')
        return HttpResponseRedirect(request.path_info)
    return render(request, 'accounts/login.html')
def register(request):
    messages.success(request,' please register first')
    if request.method == 'POST':
        firstname = request.POST.get("firstname")
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = email)

        if user_obj.exists():
            messages.warning(request, 'email is already taken')
            return HttpResponseRedirect(request.path_info)
        
        user_obj = User.objects.create_user(first_name = firstname, last_name = lastname, email=email,username=email)
        user_obj.set_password(password)
        user_obj.save()

        messages.warning(request, 'an email has been sent to your email')
        return HttpResponseRedirect(request.path_info)
    else:    
        return render(request, 'accounts/registration.html')