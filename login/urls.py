# coding:utf-8
from django.urls import path
import login.views

urlpatterns = [
    path('login/',login.views.login,),
    path('',login.views.login,),
    path('login_success/', login.views.login_success, ),
]
