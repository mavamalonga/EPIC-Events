from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django import forms
from django import forms
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
	client_form = forms.ClientForm()
	if request.method == 'POST':
		data = {
			'first_name': request.POST['first_name'],
			'last_name' : request.POST['last_name'],
			'email': request.POST['last_name'],
			'phone': request.POST['phone'],
			'mobile': request.POST['mobile'],
			'company_name': request.POST['company_name'],
			'sales_contact_id': request.POST['sales_contact_id']
		}
		r = requests.post('http://127.0.0.1:8000/api/client/', data=data)
		return redirect('client')
	context = {'client_form': client_form}
	return render(request, 'client/client_add.html', context)

def client_edit(request, client_id):
	r = requests.get('http://127.0.0.1:8000/api/client/' + str(client_id))
	if r.status_code == 200:
		if request.method == 'GET':
			initial = {
				'first_name': r.json()['first_name'],
				'last_name' : r.json()['last_name'],
				'email': r.json()['last_name'],
				'phone': r.json()['phone'],
				'mobile': r.json()['mobile'],
				'company_name': r.json()['company_name'],
				'sales_contact_id': r.json()['sales_contact_id']
			}
			client_form = forms.ClientForm(initial=initial)
			context = {'client_form': client_form}
			return render(request, 'client/client_edit.html', context)
		if request.method == 'POST':
			data = {
				'first_name': request.POST['first_name'],
				'last_name' : request.POST['last_name'],
				'email': request.POST['last_name'],
				'phone': request.POST['phone'],
				'mobile': request.POST['mobile'],
				'company_name': request.POST['company_name'],
				'sales_contact_id': request.POST['sales_contact_id']
			}
			r = requests.put('http://127.0.0.1:8000/api/client/' + str(client_id)+'/', data=data)
			return redirect('client')

def client_delete(request, client_id):
	r = requests.delete('http://127.0.0.1:8000/api/client/' + str(client_id))
	print(r.status_code)
	return redirect('client')


