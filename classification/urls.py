# coding:utf-8
from django.urls import path
import classification.views

urlpatterns = [
    path('',classification.views.index,),
    path('index', classification.views.a_index, name='index'),
]