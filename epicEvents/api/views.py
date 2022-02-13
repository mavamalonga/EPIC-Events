from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from datetime import datetime
from api.permissions import StaffAccessPermission, UserAccessPermission, ClientAccessPermission
from . import models, serializers

import psycopg2


class UserViewset(ModelViewSet, StaffAccessPermission):

	permission_classes = [IsAuthenticated, StaffAccessPermission, UserAccessPermission]
	serializer_class = serializers.UserSerializer

	def get_queryset(self):
		return models.User.objects.all()


class ClientViewset(ModelViewSet, StaffAccessPermission):

	permission_classes = [IsAuthenticated, StaffAccessPermission, ClientAccessPermission]
	serializer_class = serializers.ClientSerializer

	def get_queryset(self):
		return models.Client.objects.all()


class EventViewset(ModelViewSet, StaffAccessPermission):

	permission_classes = [IsAuthenticated, StaffAccessPermission]
	serializer_class = serializers.EventSerializer

	def get_queryset(self):
		return models.Event.objects.all()


class ContractViewset(ModelViewSet, StaffAccessPermission):

	permission_classes = [IsAuthenticated, StaffAccessPermission]
	serializer_class = serializers.ContractSerializer

	def get_queryset(self):
		return models.Contract.objects.all()

