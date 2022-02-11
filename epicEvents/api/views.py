from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from datetime import datetime
from . import models, serializers


class UserViewset(ModelViewSet):

	serializer_class = serializers.UserSerializer

	def get_queryset(self):
		return models.User.objects.all()


class ClientViewset(ModelViewSet):

	serializer_class = serializers.ClientSerializer

	def get_queryset(sel):
		return models.Client.objects.all()


class EventViewset(ModelViewSet):

	serializer_class = serializers.EventSerializer

	def get_queryset(self):
		return models.Event.objects.all()


class ContractViewset(ModelViewSet):

	serializer_class = serializers.ContractSerializer

	def get_queryset(self):
		return models.Contract.objects.all()

