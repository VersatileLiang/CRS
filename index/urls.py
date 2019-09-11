# coding:utf-8
from django.urls import path
import index.views

urlpatterns = [
    path('index/',index.views.index,),
    path('',index.views.index,),
]