from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from api import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/sign-up/', views.SignUpView.as_view(), name='sign-up'),
    path('api/login/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('api/clients/', views.ClientView.as_view(), name='clients'),
    path('api/client/<int:client_id>/', views.ClientViewDetail.as_view(), name='client'),
    path('api/events/', views.EventView.as_view(), name='events'),
    path('api/event/<int:event_id>/', views.EventViewDetail.as_view(), name='event')
]
