from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from datetime import datetime
from . import models, serializers
from api.permissions import StaffAccessPermission, UserAccessPermission, \
	ClientAccessPermission, EventAccessPermission, ContractAccessPermission

import psycopg2


class UserViewset(ModelViewSet, StaffAccessPermission, 
		UserAccessPermission):

	permission_classes = [IsAuthenticated, StaffAccessPermission, 
		UserAccessPermission]
	serializer_class = serializers.UserSerializer

	def get_queryset(self):
		return models.User.objects.all()


class ClientViewset(ModelViewSet, StaffAccessPermission, 
		ClientAccessPermission):

	permission_classes = [IsAuthenticated, StaffAccessPermission, 
		ClientAccessPermission]
	serializer_class = serializers.ClientSerializer

	def get_queryset(self):
		if self.request.user.groups.filter(name='team-support').exists() == True:
			my_clients = []
			for event in models.Event.objects.filter(support_contact_id=self.request.user.id):
				my_clients.append(event.client_id.id)
			return models.Client.objects.filter(pk__in=my_clients)
		elif self.request.user.groups.filter(name='team-vente').exists() == True:
			my_clients = []
			for client in models.Client.objects.filter(sales_contact_id=self.request.user.id):
				my_clients.append(client.id)
			return models.Client.objects.filter(pk__in=my_clients)
		else:
			return models.Client.objects.all()


class EventViewset(ModelViewSet, StaffAccessPermission, 
		EventAccessPermission):

	permission_classes = [IsAuthenticated, StaffAccessPermission, 
		EventAccessPermission]
	serializer_class = serializers.EventSerializer

	def get_queryset(self):
		if self.request.user.groups.filter(name='team-support').exists() == True:
			return models.Event.objects.filter(support_contact_id=self.request.user.id)
		elif self.request.user.groups.filter(name='team-vente').exists() == True:
			my_clients = []
			for client in models.Client.objects.filter(sales_contact_id=self.request.user.id):
				my_clients.append(client.id)
			return models.Event.objects.filter(client_id__in=my_clients)
		else:
			return models.Event.objects.all()


class ContractViewset(ModelViewSet, StaffAccessPermission, 
		ContractAccessPermission):

	permission_classes = [IsAuthenticated, StaffAccessPermission, 
		ContractAccessPermission]
	serializer_class = serializers.ContractSerializer

	def get_queryset(self):
		my_events = []
		if self.request.user.groups.filter(name='team-support').exists() == True:
			for event in models.Event.objects.filter(support_contact_id=self.request.user.id):
				my_events.append(event.id)
			return models.Contract.objects.filter(event_id__in=my_events)
		elif self.request.user.groups.filter(name='team-vente').exists() == True:
			return models.Contract.objects.filter(sales_contact_id=self.request.user.id)
		else:
			return models.Contract.objects.all()

