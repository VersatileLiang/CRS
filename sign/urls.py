# coding:utf-8
from django.urls import path
import sign.views

urlpatterns = [
    path('',sign.views.index,),
    path('sign',sign.views.sign)
]