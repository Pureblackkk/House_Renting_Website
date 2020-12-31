from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns=[
    path('login/', views.login),
    path('user/', views.userEnter),
    path('test/', views.test),
    path('usrSearch/', views.userSearch),
    path('hostSearch/', views.hostSearch),
    path('hostUpdate/', views.hostUpdate)
 ]