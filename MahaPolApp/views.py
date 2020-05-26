from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
import datetime
import hashlib
import os
# Create your views here.

def register(request):
	context = {}
	return render(request, "signup-page.html", context)

def login(request):
	context = {}
	return render(request, "login-page.html", context)