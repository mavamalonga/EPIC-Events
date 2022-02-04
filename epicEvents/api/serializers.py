from rest_framework.serializers import ModelSerializer, SerializerMethodField, ValidationError
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from . import models


class SignUpSerializer(ModelSerializer):
	email = serializers.EmailField(
		required=True, 
		validators=[UniqueValidator(queryset=models.User.objects.all())]
	)
	password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
	password2 = serializers.CharField(write_only=True, required=True)

	class Meta:
		model = models.User
		fields = ('username', 'email', 'password', 'password2')

	def validate(self, attrs):
		if attrs['password'] != attrs['password2']:
			raise serializers.ValidationError({"password":"Password fields didn't match."})
		return attrs

	def create(self, validated_data):
		user = models.User.objects.create(
			username=validated_data['username'],
			email=validated_data['email']
		)
		user.set_password(validated_data['password'])
		user.save()
		return user


class ClientSerializer(ModelSerializer):
	class Meta:
		model = models.Client
		fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'mobile',
			'company_name', 'date_created', 'date_updated', 'sales_contact_id']


class ClientSerializerPost(ModelSerializer):
	class Meta:
		model = models.Client
		fields = ['first_name', 'last_name', 'email', 'phone', 'mobile',
			'company_name','sales_contact_id']

