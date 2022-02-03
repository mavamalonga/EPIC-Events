from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


import authentication.views
import app.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authentication.views.signIn, name='login'),
    path('login/', authentication.views.signIn, name='login'),
    path('sign-up/', authentication.views.signUp, name='sign-up'),
    path('logout/', authentication.views.logoutUser, name='logout'),
    path('index/', app.views.index, name='index')
]
