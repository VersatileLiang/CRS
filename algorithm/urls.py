# coding:utf-8
from django.urls import path
import algorithm.views

urlpatterns = [
    path('',algorithm.views.index,),
]