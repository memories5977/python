import requests
from bs4 import BeautifulSoup

def getContent():
    content = requests.get("http://www.qiushibaike.com").content
    soup = BeautifulSoup(content, 'html.parser')
    i = 0;
    for div in soup.find_all('div', {'class':'content'}):
        i+=1
        print(str(i)+'. '+div.span.text)

def string_demo():
    stra = 'hello world'
    # capitalize()实现首字母大写，其余变小写
    print(stra.capitalize())
    print(stra.replace('hello', 'hehe'))
    stra = ' \n\r  hello world\n\r'
    # lstrip()方法为去掉字符串头部的回车换行空格等
    # rstrip()方法为去掉字符串尾部的回车换行空格等
    print(stra.lstrip())
    print(len(stra))
    # 用_把三个字符串连起来
    print('_'.join(['a', 'b', 'c']))

def buildinfunction_demo():
    a = 1;
    print(type(a))
    print(max(2, 1))
    print(min(2, 3))
    print(len([1,2,4]))
    print(abs(-1))
    # 从1到10，步长为3
    print(list(range(1, 10, 3)))
    # eval函数直接计算表达式，不用实现后缀表达式
    expression = '(1+2/2)*2'
    print(eval(expression))
    # chr()将数字转换为字符
    print(chr(95))
    # ord() 将字符转为数字 asscii码
    print(ord('a'))

def controlflow_demo():
    a = 90
    if a > 90:
        print('A')
    elif a > 80:
        print('B')
    else:
        print('C')


    # pass:没有任何作用，只起到占位的作用；continue、break作用与Java相同
    for i in range(0, 10, 2):
        print(i)

def list_demo():
    lista = [1, 2, 3]
    listb = ['a', 'b', 3, 4]
    # 将listb中所有元素追加到lista中
    lista.extend(listb)
    print(lista)
    # 合并lista和listb到新的list
    print(lista+listb)
    # lista.sort(reverse=True)
    # 复制list中元素，长度加倍
    lista * 2
    # tuple的长度不能改变
    t1 = (1, 2)
    print(type(t1))

def dictionary_demo():
    dicta = {1:1, 2:4, 3:9}
    print(dicta)
    print(dicta.keys())
    print(dicta.values())

    for k, v in dicta.items():
        print(str(k) + ' ' + str(v))

def set_demo():
    # set通过set()构造函数进行构造，参数是一个list或tuple，内部元素不重复
    # 不同set可通过&、|进行求交集和并集
    seta = set([1,2,4,4])
    print(seta)

class User:
    type = 'USER'


# 相当于Java的main方法，即程序执行的入口
if __name__ == '__main__':
    set_demo()