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

def register_user(request):
	context = {}
	x = datetime.datetime.now()
	date = x.strftime("%c")
	if request.method == "POST":
		data = request.POST
		password1 = data['password1']
		passwordenc = hashlib.sha256(password1.encode())
		passwordenc = passwordenc.hexdigest()
		rd = register_data(first_name=data['fname'], last_name=data['lname'], dob=data['dob'], mobile=data['mobno'], address=data['address'], user_name=data['username'], email=data['email'], password=passwordenc, created_on=date)
		rd.save()
		context = {'status':'success'}
	return redirect('register_success')

def register_success(request):
	context = {}
	return render(request, "sign-up-success.html", context)

def login(request):
	context = {}
	return render(request, "login-page.html", context)