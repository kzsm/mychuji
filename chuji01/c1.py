
# -*- coding:utf-8 -*-
import random
import re

import requests
from bs4 import BeautifulSoup



def qiushibaike():
    content = requests.get('https://www.qiushibaike.com/').content
    soup = BeautifulSoup(content, 'html.parser')

    for div in soup.find_all('div', {'class': 'content'}):
        print div.text.strip()


def demo_string():
    stra = 'hello NiHao'
    print stra.capitalize()
    print stra.replace('hello', 'nihao')


def demo_buildfunction():
    print max(23, 56)
    print 2, len('XXX'), len([2, 5, 7])
    print 3, abs(-25)
    print 4, range(1, 10, 3)
    print 5, dir(list)
    x = 2
    print 6, eval('x+3')
    print 7, divmod(15, 3)


def demo_if():
    score = 65
    if score > 80:
        print 1, 'A'
    elif score > 60:
        print 2, 'B'
    else:
        print 3, 'C'

    for i in range(1, 10):
        print i


def demo_list():
    lista = ['sjfk', 23, 'hojj']
    listb = [12, 34, 44.4]
    lista.extend(listb)
    print lista
    print len(lista)
    lista.sort(reverse=True)
    print lista
    lista.sort()
    print lista


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def demo_dict():
    dicta = {4: 25, 45: 78, 89: 78}
    for key, value in dicta.items():
        print key, value
    dictb = {'+': add, '-': sub}
    print 1, dictb.get('+')(6.7, 78)
    print 2, dictb['-'](7897598, 23868)


class User:
    type = 'USER'

    def __init__(self, name, uid):
        self.name = name
        self.uid = uid

    def __repr__(self):
        return 'im ' + self.name + ' ' + str(self.uid)


class Admin(User):
    type = 'ADMIN'

    def __init__(self, name, uid, group):
        User.__init__(self, name, uid)
        self.group = group

    def __repr__(self):
        return 'Im' + self.name + ' ' + str(self.uid) + ' ' + str(self.group)


def demo_random():
    random.seed(10)
    print 1,int(random.random()*10)
    print 2,random.randint(10,20)
    print 3,random.choice(range(1,100,10))
    print 4,random.sample(range(3,10),3)

def demo_re():
    str='ajskdfk32443dfjgk365564'
    p1=re.compile('[\d]+')
    print p1.findall(str)

    str='adjfk@163.com;shsh12@qq.com;nihao@126.com'
    p2=re.compile('[\w]+@163\.com')
    print p2.findall(str)
    p2=re.compile('[\w]+@[163|qq]+\.com')
    print p2.findall(str)



if __name__ == '__main__':
    '''
    user1 = User('u1', 10)
    print user1.__repr__()

    ad = Admin('a1', 20, 5)
    print ad.__repr__()
    '''
    # print "hello now"
    # comment
    # demo_dict()
    demo_re()
