from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from datetime import datetime
from . import models, serializers
from . permissions import StaffAccessPermission, UserAccessPermission, \
	ClientAccessPermission, EventAccessPermission, ContractAccessPermission

import psycopg2


class UserViewset(ModelViewSet):

	permission_classes = [IsAuthenticated, StaffAccessPermission, UserAccessPermission]
	serializer_class = serializers.UserSerializer

	def get_queryset(self):
		return models.User.objects.all()


class ClientViewset(ModelViewSet):

	permission_classes = [IsAuthenticated, StaffAccessPermission, ClientAccessPermission]
	serializer_class = serializers.ClientSerializer

	def get_queryset(self):
		return models.Client.objects.all()


class EventViewset(ModelViewSet):

	permission_classes = [IsAuthenticated, StaffAccessPermission, EventAccessPermission]
	serializer_class = serializers.EventSerializer

	def get_queryset(self):
		return models.Event.objects.all()


class ContractViewset(ModelViewSet):

	permission_classes = [IsAuthenticated, StaffAccessPermission, ContractAccessPermission]
	serializer_class = serializers.ContractSerializer

	def get_queryset(self):
		return models.Contract.objects.all()

