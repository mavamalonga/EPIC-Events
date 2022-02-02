from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):

	def __str__(self):
		return self.first_name


class Client(models.Model):

	first_name = models.CharField(max_length=25)
	last_name = models.CharField(max_length=25)
	email = models.CharField(max_length=200)
	phone = models.CharField(max_length=20)
	mobile = models.CharField(max_length=20)
	comapny_name = models.CharField(max_length=250)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField()

	def __str__(self):
		return self.first_name


class Event(models.Model):

	name = models.CharField(max_length=50)
	description = models.TextField(max_length=8192, blank=True)
	date = models.DateTimeField()
	address = models.CharField(max_length=200)
	client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
	assignee_id = models.ForeignKey(User, on_delete=models.CASCADE)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField()

	def __str__(self):
		return self.name

class Contract(models.Model):

	notes = models.TextField(max_length=8192)
	event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
	client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
	assignee_id = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateTimeField()

