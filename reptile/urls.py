# coding:utf-8
from django.urls import path
import reptile.views

urlpatterns = [
    path('',reptile.views.index,),
]