from rest_framework.viewsets import ModelViewSet
from . import models, serializers
from api import permissions

class UserViewset(ModelViewSet):
	permission_classes = [permissions.StaffAccessPermission,
	permissions.UserAccessPermission]
	serializer_class = serializers.UserSerializer

	def get_queryset(self):
		return models.User.objects.all()


class ClientViewset(ModelViewSet):
	permission_classes = [permissions.StaffAccessPermission,
	permissions.ClientAccessPermission]
	serializer_class = serializers.ClientSerializer

	def get_queryset(self):
		return models.Client.objects.all()


class EventViewset(ModelViewSet):
	permission_classes = [permissions.StaffAccessPermission,
	permissions.EventAccessPermission]
	serializer_class = serializers.EventSerializer

	def get_queryset(self):
		return models.Event.objects.all()


class ContractViewset(ModelViewSet):
	permission_classes = [permissions.StaffAccessPermission,
	permissions.ContractAccessPermission]
	serializer_class = serializers.ContractSerializer

	def get_queryset(self):
		return models.Contract.objects.all()
