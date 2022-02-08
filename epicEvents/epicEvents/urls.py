from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import api.views
import client.views

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/sign-up/', api.views.SignUpView.as_view(), name='api-sign-up'),
    path('api/login/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('api/client/', api.views.ClientView.as_view(), name='api-client'),
    path('api/client/<int:client_id>/', api.views.ClientViewDetail.as_view(), name='api-client-details'),
    path('api/event/', api.views.EventView.as_view(), name='api-event'),
    path('api/event/<int:event_id>/', api.views.EventViewDetail.as_view(), name='api-event-details'),
    path('api/contract/', api.views.ContractView.as_view(), name='api-contract'),
    path('api/contract/<int:contract_id>/', api.views.ContractViewDetail.as_view(), name='api-contract-details'),
    path('client/', client.views.client, name='client'),
    path('client/<int:client_id>/', client.views.client_details, name='client-details'),
    path('client/add/', client.views.client_add, name='client-add')
]
