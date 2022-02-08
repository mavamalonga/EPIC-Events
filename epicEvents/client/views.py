from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from client import forms

import requests


def client(request):
	r = requests.get('http://127.0.0.1:8000/api/client')
	if r.status_code == 200:
		clients = r.json()
		context = {'clients': clients}
	return render(request, 'client/client.html', context)

def client_details(request, client_id):
	r = requests.get('http://127.0.0.1:8000/api/client/' + str(client_id))
	if r.status_code == 200:
		client = r.json()
		context = {'client': client}
	return render(request, 'client/client_details.html', context)

def client_add(request):
	pass

def client_edit(request, client_id):
	r = requests.get('http://127.0.0.1:8000/api/client/' + str(client_id))
	if r.status_code == 200:
		if request.method == 'GET':
			client_form = forms.ClientForm()

