from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from authentication import forms
from django.conf import settings


def signUp(request):
	form = forms.SignUpForm()
	if request.method == 'POST':
		form = forms.SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect(settings.LOGIN_REDIRECT_URL)
	return render(request, 'authentication/SignUp.html', {'form': form, 'page_name': None })


def SignIn(request):
	form = forms.LoginForm()
	message = ''
	if request.method == 'POST':
		form = forms.LoginForm(request.POST)
		if form.is_valid():
			user = authenticate(
				username=form.cleaned_data['username'],
				password=form.cleaned_data['password'],
			)
			if user is not None:
				login(request, user)
				return redirect('index')
			else:
				message = 'Identifiants invalides'
	return render(request, 'authentication/login.html', {'form': form,
		'message': message, 'page_name': None})


def logoutUser(request):
	logout(request)
	return redirect('login')


