from django.shortcuts import render
import re
import requests
from urllib import error
from bs4 import BeautifulSoup
import os

from CarrierRecognitionSystem import settings

num = 0
numPicture = 0
file = ''
List = []
# Create your views here.
def index(request):
    return render(request, 'reptile/reptilePage.html')
def reptile(request):
    word = request.POST.get("dataOrigin")
    # add = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%E5%BC%A0%E5%A4%A9%E7%88%B1&pn=120'
    url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + word + '&pn='
    # tot = Find(url)
    # Recommend = recommend(url)  # 记录相关推荐
    # print('经过检测%s类图片共有%d张' % (word, tot))
    numPicture =20
    file =os.path.join(settings.BASE_DIR, 'static/images')
    y = os.path.exists(file)
    t = 0
    tmp = url
    while t < numPicture:
        try:
            url = tmp + str(t)
            result = requests.get(url, timeout=10)
            print(url)
        except error.HTTPError as e:
            print('网络错误，请调整网络后重试')
            t = t + 60
        else:
            global num
            # t =0
            pic_url = re.findall('"objURL":"(.*?)",', result.text, re.S)  # 先利用正则表达式找到图片url
            print('找到关键词:' + word + '的图片，即将开始下载图片...')
            for each in pic_url:
                print('正在下载第' + str(num + 1) + '张图片，图片地址:' + str(each))
                try:
                    if each is not None:
                        pic = requests.get(each, timeout=7)
                    else:
                        continue
                except BaseException:
                    print('错误，当前图片无法下载')
                    continue
                else:
                    string = file + r'\\' + word + '_' + str(num) + '.jpg'
                    fp = open(string, 'wb')
                    fp.write(pic.content)
                    fp.close()
                    num += 1
                if num >= numPicture:
                    break
            t = t + 60
    return render(request, 'reptile/reptilePage.html')