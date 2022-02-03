from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from authentication import forms
from django.conf import settings


def index(request):
	return render(request, 'app/index.html', {'message': 'Hello word!'})