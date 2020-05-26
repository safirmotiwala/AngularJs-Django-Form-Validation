from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
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
	if request.method=="POST":
		data = request.POST
		username = data['username']
		password = data['password']
		passwordenc = hashlib.sha256(password.encode())
		passwordenc = passwordenc.hexdigest()
		l = register_data.objects.filter(user_name=username, password=passwordenc)
		if len(l)>0:
			l = l[0]
			request.session["user_id"] = l.id
			request.session["fname"] = l.first_name
			request.session['lname'] = l.last_name
			request.session['dob'] = l.dob
			request.session['mobno'] = l.mobile
			request.session['address'] = l.address
			request.session['username'] = l.user_name
			request.session['email'] = l.email
			request.session["is_authenticated"]=True
			messages.add_message(request, messages.INFO,'Login Successfull')
			return render(request, "index.html", {})
		context = {'message1':'Username or Password is incorrect'}
	return render(request, "login-page.html", context)

def logout(request):
	del request.session["user_id"]
	del request.session["fname"]
	del request.session['lname']
	del request.session['dob']
	del request.session['mobno']
	del request.session['address']
	del request.session['username']
	del request.session['email']
	del request.session["is_authenticated"]
	return redirect('login')

def home(request):
	context = {}
	return render(request, "index.html", context)