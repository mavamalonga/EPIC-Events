from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views import ContractViewset, EventViewset, ClientViewset, UserViewset


router = routers.SimpleRouter()
router.register('contract', ContractViewset, basename='contract')
router.register('event', EventViewset, basename='event')
router.register('client', ClientViewset, basename='client')
router.register('user', UserViewset, basename='user')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls))
]
