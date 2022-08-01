from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from api import models


class UserSerializer(ModelSerializer):
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
		fields = "__all__"


class EventSerializer(ModelSerializer):
	class Meta:
		model = models.Event
		fields = fields = "__all__"


class ContractSerializer(ModelSerializer):
	class Meta:
		model = models.Contract
		fields =  fields = "__all__"