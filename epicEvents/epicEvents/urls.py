from django.contrib import admin
<<<<<<< HEAD
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import api.views

=======
from django.urls import path, include
from rest_framework import routers
>>>>>>> api
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views import ContractViewset, EventViewset, ClientViewset, UserViewset

# Ici nous créons notre routeur
router = routers.SimpleRouter()
router.register('contract', ContractViewset, basename='contract')
router.register('event', EventViewset, basename='event')
router.register('client', ClientViewset, basename='client')
router.register('user', UserViewset, basename='user')


urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('api/sign-up/', api.views.SignUpView.as_view(), name='api-sign-up'),
    path('api/login/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('api/client/', api.views.ClientView.as_view(), name='api-client'),
    path('api/client/<int:client_id>/', api.views.ClientViewDetail.as_view(), name='api-client-details'),
    path('api/event/', api.views.EventView.as_view(), name='api-event'),
    path('api/event/<int:event_id>/', api.views.EventViewDetail.as_view(), name='api-event-details'),
    path('api/contract/', api.views.ContractView.as_view(), name='api-contract'),
    path('api/contract/<int:contract_id>/', api.views.ContractViewDetail.as_view(), name='api-contract-details')
=======
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls))
>>>>>>> api
]
