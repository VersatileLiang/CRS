import re
import requests
from matplotlib import pyplot as plt
from matplotlib import font_manager
import matplotlib.pyplot as plt
import numpy as np

font = {
        'family': 'SimHei'
    }
plt.rc('font', **font)

def get_author(url):
    Result = requests.get(url, timeout=5)
    pic_url = re.findall('<a title="(.*?)" ', Result.text, re.S)
    return pic_url

def max_count(lt):
    d = {}
    max_key = None
    for i in lt:
        if i not in d:
            count = lt.count(i)
            d[i] = count
            if count > d.get(max_key, 0):
                if i.find("出版") == -1:
                    max_key = i
    return max_key

def max_num(lt):
    d = {}
    max_key = None
    max_num = 0
    for i in lt:
        if i not in d:
            count = lt.count(i)
            d[i] = count
            if count > d.get(max_key, 0):
                if i.find("出版") == -1:
                    max_key = i
                    max_num = count
    return max_num

if __name__ == '__main__':
    List = []
    list1 = []
    url = 'https://list.jd.com/list.html?cat=1713,3258,3304'
    word = "侦探悬疑"
    tot = get_author(url)
    print(tot)
    print('经过检测%s类作者出现次数最多的是%s，共出现%d次' % (word, max_count(tot), max_num(tot)))
    List.append(max_count(tot))
    list1.append(max_num(tot))

    url = 'https://list.jd.com/list.html?cat=1713,3258,6569'
    word = "科幻"
    tot = get_author(url)
    print(tot)
    print('经过检测%s类作者出现次数最多的是%s，共出现%d次' % (word, max_count(tot), max_num(tot)))
    List.append(max_count(tot))
    list1.append(max_num(tot))

    url = 'https://list.jd.com/list.html?cat=1713,3258,3316'
    word = "官场"
    tot = get_author(url)
    print(tot)
    print('经过检测%s类作者出现次数最多的是%s，共出现%d次' % (word, max_count(tot), max_num(tot)))
    List.append(max_count(tot))
    list1.append(max_num(tot))

    url = 'https://list.jd.com/list.html?cat=1713,3258,3317'
    word = "历史"
    tot = get_author(url)
    print(tot)
    print('经过检测%s类作者出现次数最多的是%s，共出现%d次' % (word, max_count(tot), max_num(tot)))
    List.append(max_count(tot))
    list1.append(max_num(tot))

    url = 'https://list.jd.com/list.html?cat=1713,3258,3306'
    word = "玄幻奇幻"
    tot = get_author(url)
    print(tot)
    print('经过检测%s类作者出现次数最多的是%s，共出现%d次' % (word, max_count(tot), max_num(tot)))
    List.append(max_count(tot))
    list1.append(max_num(tot))

    url = 'https://list.jd.com/list.html?cat=1713,3258,3312'
    word = "都市"
    tot = get_author(url)
    print(tot)
    print('经过检测%s类作者出现次数最多的是%s，共出现%d次' % (word, max_count(tot), max_num(tot)))
    List.append(max_count(tot))
    list1.append(max_num(tot))

    url = 'https://list.jd.com/list.html?cat=1713,3258,3308'
    word = "军事"
    tot = get_author(url)
    print(tot)
    print('经过检测%s类作者出现次数最多的是%s，共出现%d次' % (word, max_count(tot), max_num(tot)))
    List.append(max_count(tot))
    list1.append(max_num(tot))

    url = 'https://list.jd.com/list.html?cat=1713,3258,3311'
    word = "社会"
    tot = get_author(url)
    print(tot)
    print('经过检测%s类作者出现次数最多的是%s，共出现%d次' % (word, max_count(tot), max_num(tot)))
    List.append(max_count(tot))
    list1.append(max_num(tot))

    url = 'https://list.jd.com/list.html?cat=1713,3258,3303'
    word = "外国小说"
    tot = get_author(url)
    print(tot)
    print('经过检测%s类作者出现次数最多的是%s，共出现%d次' % (word, max_count(tot), max_num(tot)))
    List.append(max_count(tot))
    list1.append(max_num(tot))

    url = 'https://list.jd.com/list.html?cat=1713,3258,3320'
    word = "世界名著"
    tot = get_author(url)
    print(tot)
    print('经过检测%s类作者出现次数最多的是%s，共出现%d次' % (word, max_count(tot), max_num(tot)))
    List.append(max_count(tot))
    list1.append(max_num(tot))

    url = 'https://list.jd.com/list.html?cat=1713,3258,3297'
    word = "当代小说"
    tot = get_author(url)
    print(tot)
    print('经过检测%s类作者出现次数最多的是%s，共出现%d次' % (word, max_count(tot), max_num(tot)))
    List.append(max_count(tot))
    list1.append(max_num(tot))

    url = 'https://list.jd.com/list.html?cat=1713,3258,3305'
    word = "惊悚恐怖"
    tot = get_author(url)
    print(tot)
    print('经过检测%s类作者出现次数最多的是%s，共出现%d次' % (word, max_count(tot), max_num(tot)))
    List.append(max_count(tot))
    list1.append(max_num(tot))

    url = 'https://list.jd.com/list.html?cat=1713,3258,3309'
    word = "情感家庭"
    tot = get_author(url)
    print(tot)
    print('经过检测%s类作者出现次数最多的是%s，共出现%d次' % (word, max_count(tot), max_num(tot)))
    List.append(max_count(tot))
    list1.append(max_num(tot))

    url = 'https://list.jd.com/list.html?cat=1713,3258,3319'
    word = "作品集"
    tot = get_author(url)
    print(tot)
    print('经过检测%s类作者出现次数最多的是%s，共出现%d次' % (word, max_count(tot), max_num(tot)))
    List.append(max_count(tot))
    list1.append(max_num(tot))

    # 添加图形属性
    plt.xlabel('Age range')
    plt.ylabel('Number')
    plt.title('The statistics of face age dataset')
    a = plt.subplot(1, 1, 1)

    plt.ylim = (10, 40000)
    x1 = List

    Y1 = list1

    # 这里需要注意在画图的时候加上label在配合plt.legend（）函数就能直接得到图例，简单又方便！

    plt.bar(x1, Y1, facecolor='red', width=3, label='1')


    plt.legend()

    plt.show()

