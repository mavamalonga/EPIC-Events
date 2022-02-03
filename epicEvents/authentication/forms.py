# authentication/forms
from django import forms
from authentication.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
	class Meta(UserCreationForm):
		model = get_user_model()
		fields = ('username', 'email')


class LoginForm(forms.Form):
	username = forms.CharField(max_length=63, label="Nom d'utilisateur")
	password = forms.CharField(max_length=63, widgets=forms.PasswordInput, label='Mot de passe')
