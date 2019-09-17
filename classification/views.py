from django import forms
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import tensorflow as tf
import os
import numpy as np
import re
from PIL import Image
import matplotlib.pyplot as plt
import shutil


# Create your views here.
from classification.models import user


def index(request):
    return render(request, 'classification/classificationPage.html')

class UserForm(forms.Form):
    username = forms.CharField(required=False)
    headImg = forms.ImageField(required=False)


@csrf_exempt
def a_index(request):
    print('aaaaaaaaaaa')
    if request.method == "POST":
        uf = UserForm(request.POST,request.FILES)
        if uf.is_valid():
            print(request.FILES)
            # 获取表单信息request.FILES是个字典
            User = user(headImg=request.FILES['file'])
            # 保存在服务器
            try:
                User.save()
            except Exception :
                print('那个异常1')

            # 算法
            lines = tf.gfile.GFile('C:/Users/hasee/Desktop/CRS/classification/output_labels.txt').readlines()  # 读取标签
            uid_to_human = {}
            # 一行一行读取数据
            for uid, line in enumerate(lines):
                # 去掉换行符
                line = line.strip('\n')
                uid_to_human[uid] = line

            path = 'C:/Users/hasee/Desktop/CRS/classification/upload/'
            # 创建一个图来存放google训练好的模型
            with tf.gfile.FastGFile('C:/Users/hasee/Desktop/CRS/classification/output_graph.pb', 'rb') as f:  # 读取模型
                graph_def = tf.GraphDef()
                graph_def.ParseFromString(f.read())
                tf.import_graph_def(graph_def, name='')
            def id_to_string(node_id):
                if node_id not in uid_to_human:
                    return ''
                return uid_to_human[node_id]

            with tf.Session() as sess:
                softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
                # 遍历目录
                for root, dirs, files in os.walk('C:/Users/hasee/Desktop/CRS/classification/upload/'):  # 存放需要测试的图片的路径
                    for file in files:
                        # 载入图片
                        image_data = tf.gfile.FastGFile(os.path.join(root, file), 'rb').read()
                        predictions = sess.run(softmax_tensor, {'DecodeJpeg/contents:0': image_data})  # 图片格式是jpg格式
                        predictions = np.squeeze(predictions)  # 把结果转为1维数据
                        # 打印图片路径及名称
                        image_path = os.path.join(root, file)
                        print(image_path)
                        # 显示图片
                        img = Image.open(image_path)
                        plt.imshow(img)
                        plt.axis('off')
                        # plt.show()
                        # 排序
                        top_k = predictions.argsort()[::-1]
                        print(top_k)
                        for node_id in top_k:
                            # 获取分类名称
                            human_string = id_to_string(node_id)
                            # 获取该分类的置信度
                            score = predictions[node_id]
                            print('%s (score = %.5f)' % (human_string, score))
                            if human_string == 'hangmu':
                                shutil.rmtree(path)
                                return HttpResponse('航母')
                            else:
                                shutil.rmtree(path)
                                return HttpResponse('船舶')
                        print()
            return HttpResponse('u')
    return render(request, 'classification/classificationPage.html')

