# coding:utf-8
from django.urls import path
import login.views

urlpatterns = [
    path('login/',login.views.login,),
    path('',login.views.login,),
    path('user_login/', login.views.login_success, ),
]