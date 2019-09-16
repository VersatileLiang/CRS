import os

from PIL import Image
from bs4 import BeautifulSoup
from django.http import HttpRequest
from django.shortcuts import render
import shutil
import requests
# Create your views here.
from CarrierRecognitionSystem import settings


def index(request):
    i = 0
    j=0
    imgpath = os.path.join(settings.BASE_DIR, 'static/images')
    for root, dirs, files in os.walk(imgpath):
        try:
            im = files[i]
        except(OSError, NameError):
            print('OSError, Path:', imgpath)
    return render(request, 'sign/signPage.html',{"url":im,"num":i,"number":j})
def sign(request):
    imgpath =os.path.join(settings.BASE_DIR, 'static/images')
    new_imgpath = 'E:/pictures/'
    jsonpath = './gt'
    new_jsonpath = './new_json'
    j = 0  # 文件名起始
    s=request.POST.get("city")
    num1=request.POST.get("number1")
    i=int(num1)
    for root, dirs, files in os.walk(imgpath):
        if(i<=len(files)):
            try:
                im = Image.open(os.path.join(imgpath, files[i]))
                if(s=="y"):
                    json_file = files[i].split('.')[0]
                    shutil.copy(os.path.join(imgpath, files[i]), os.path.join(new_imgpath, str("是")+str(i)+ '.jpg'))
                if(s=="n"):
                    json_file = files[i].split('.')[0]
                    shutil.copy(os.path.join(imgpath, files[i]), os.path.join(new_imgpath, str("非")+str(i)+ '.jpg'))
            except(OSError, NameError):
                print('OSError, Path:', imgpath)
    i=i+1
    im=files[i]
    return render(request, 'sign/signPage.html', {"url": im, "num": i,"number":j})

