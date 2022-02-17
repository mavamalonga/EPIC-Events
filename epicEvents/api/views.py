from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from datetime import datetime
from . import models, serializers
from api.permissions import StaffAccessPermission, UserAccessPermission, \
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

	def update(self, request, pk=None):
		client = get_object_or_404(models.Client, pk=pk)
		serializer = serializers.ClientSerializer(client, data=request.data)
		if serializer.is_valid():
			if client.sales_contact_id.id == request.user.id:
				serializer.save()
				return Response(status=status.HTTP_200_OK)
			else:
				return Response({"detail": "Permission only to the sales contact of client."},
					status=status.HTTP_403_FORBIDDEN)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk=None):
		client = get_object_or_404(models.Client, pk=pk)
		if client.sales_contact_id.id == request.user.id:
			client.delete()
			return Response(status=status.HTTP_200_OK)
		else:
			return Response({"detail": "Permission only to the sales contact of client."},
				status=status.HTTP_403_FORBIDDEN)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



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

	def update(self, request, pk=None):
		contract = get_object_or_404(models.Contract, pk=pk)
		serializer = serializers.ContractSerializerS(contract, data=request.data)
		if serializer.is_valid():
			if contract.sales_contact_id.id == request.user.id:
				serializer.save()
				return Response(status=status.HTTP_200_OK)
			else:
				return Response({"detail": "Permission only to the sales contact of client."},
					status=status.HTTP_403_FORBIDDEN)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk=None):
		contract = get_object_or_404(models.Contract, pk=pk)
		if contract.sales_contact_id.id == request.user.id:
			contract.delete()
			return Response(status=status.HTTP_200_OK)
		else:
			return Response({"detail": "Permission only to the sales contact of client."},
				status=status.HTTP_403_FORBIDDEN)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
