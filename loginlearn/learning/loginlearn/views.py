from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import User
from django.http import request
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError

# Create your views here.
def index(request):
    return HttpResponse("this is a index page")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("index"))
        else:
            context = {
                "message" : "Invalid credentials"
            }
            return render ( request, "usermaking/login.html", context)
    else:
        return render(request, "loginlearn/login.html")
    

def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        submit = request.POST["register"]
        if password != confirmation:
            context = {
                "message" : "invalid password"
            }
            return render(request, "loginlearn/register.html",context)
        try:
            user = User.objects.create_user(username = username, password = password)
            user.save()
            login(request,user)
            return HttpResponseRedirect(reverse("index"))
        except IntegrityError:
            context = {
                "message" : "username already exists"
            }
            return render (request, "loginlearn/register.html")
        
    else:
        return render (request,"loginlearn/register.html")