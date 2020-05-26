from django.db import models

# Create your models here.

class register_data(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	dob = models.CharField(max_length=30)
	mobile = models.CharField(max_length=20)
	address = models.CharField(max_length=150)
	user_name = models.CharField(max_length=30)
	email = models.CharField(max_length=30)
	password = models.CharField(max_length=100)
	created_on = models.CharField(max_length=30)