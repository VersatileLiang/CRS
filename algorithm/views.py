from django.shortcuts import render
from django.shortcuts import render,render_to_response
from django import forms
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def index(request):
    return render(request, 'algorithm/algorithmPage.html')

