from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, "shoe/index.html")

def shopingpage(request):
    return render(request, "shoe/buyingpage.html")