from django.shortcuts import render
# from django import request
from django.http import HttpResponse, HttpResponseRedirect
from  .models import *
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from datetime import date
# Create your views here.
def index(request):
    if request.method == "POST":
        task = request.POST["task"]
        newTask = Task(title = task)
        newTask.save()
        tasks = Task.objects.all()
        # print(tasks)
        context = {
            "tasks": tasks,
        }
        return render(request, "loger/index.html", context)
    else:
        tasks = Task.objects.all()
        context = {
            "tasks": tasks
        }
        return render(request, "loger/index.html", context)

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
        else:
            context = {
                "message" : "Invalid user"
            }
            return render(request, "loger/login.html", context)

            
    else:
        return render(request, "loger/login.html")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        confirmpassword = request.POST["confirmpassword"]
        submit = request.POST["submit"]
        if password != confirmpassword:
            context = {
                "message" : "password incorrect"
            }
            return render(request, "loger/register.html",context)
        
        try:
            user = User.objects.create_user(username = username, password = password)
            user.save()
            login(request, user)
            context = {
                "message" : f"hii, {user.username}"
            }
            return HttpResponseRedirect(reverse(index), context)
        except:
            context = {
                "message" : f"user already exists"
            }
            return render(request, "loger/register.html", context)
    
    else:
        return render(request, "loger/register.html")