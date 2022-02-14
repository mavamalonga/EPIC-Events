from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):

	def __str__(self):
		return self.first_name


class Client(models.Model):

	first_name = models.CharField(max_length=25, null=False)
	last_name = models.CharField(max_length=25, null=False)
	email = models.CharField(max_length=200, null=False)
	phone = models.CharField(max_length=20, null=False)
	mobile = models.CharField(max_length=20, null=False)
	company_name = models.CharField(max_length=250, null=False)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(null=True)
	sales_contact_id = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.first_name


class Event(models.Model):

	name = models.CharField(max_length=50)
	description = models.TextField(max_length=8192, blank=True)
	date = models.DateTimeField()
	address = models.CharField(max_length=200)
	client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
	support_contact_id = models.ForeignKey(User, on_delete=models.CASCADE)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(null=True)

	def __str__(self):
		return self.name

class Contract(models.Model):

	notes = models.TextField(max_length=8192)
	event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
	client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
	sales_contact_id = models.ForeignKey(User, on_delete=models.CASCADE)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(null=True)
	amount = models.FloatField()
	payment_status = models.BooleanField(default=False, verbose_name='payment_status')

	def __str__(self):
		return str(self.event_id)