__author__ = "那位先生Beer"
#打印文件夹下的文件路径
# import  os
# def print_filepath(path):
#     file_list=os.listdir(path)
#     for i in file_list:
#         print(os.path.realpath(i))
# print_filepath('G:\Python网上教学视频')

# def zhuangshiqi(func):
#     def inner(s):
#         word=func(s)
#         return word.capitalize()
#     return inner
# @zhuangshiqi
# def inputS(s):
#     return s.lower()
#
# print(inputS('qkqkqkkq'))


# def word_group(word):
#     word = word.lower()
#     dict = {}
#     list = []
#     for letter in word:
#         if not dict:
#             list.append(letter)
#             list.append(letter.upper())
#             dict[word.index(letter)] = list
#         else:
#             list = []
#             for i in dict[word.index(letter)-1] :
#                 list.append(i + letter)
#                 list.append(i+ letter.upper())
#                 dict[word.index(letter)] = list
#     print(dict[len(word)-1])
# word_group('abcdef')



# import re
# str = "\<a href=www.baidu.com\>正则表达式题库\</a>\<a href=www.cdtest.cn\>\</a>"
# regex = r"href=(.*?)\\>"
# ret_list = re.findall(regex,str)
# print(ret_list)

# str = "1.2.3.4.5"
# li = str.split(".") # li = [1,2,3,4,5]
# # 列表倒序
# li = li[::-1] # li = list(reversed(li)) 或者 li = sorted(li,reverse=True)
# # 字符串拼接
# str = "|".join(li)
# print(str)
# print('sss'.join(['1','2']))

# li = [{"k":14,"v":15},{"k":12,"v":22},{"k":13,"v":32}]
# li.sort(key=lambda dict:dict["k"],reverse=True)
# print(li)

#枚举函数
# seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# print(list(enumerate(seasons,start = 1)))
# for i, element in enumerate(seasons):
#     print(i, element)



#
# import re
# data_info = "现在的时间是：2018-3-10 11:52"
# regex = r"\d{4}-\d{1,2}-\d{1,2}\s\d{1,2}:\d{2}"
# ret = re.search(regex,data_info)
# print(type(ret))

# d = {'k1':'hh','k2':'kk'}
# print(d.items())


#元祖元素不可变，元祖元素的元素可变
# a = ([1,3],3,4,5)
# a[0].remove(1)
# print(a)


#生成器# 简单的生成器函数
# def my_gen():
#      n=1
#      print("first")
#      # yield区域
#      yield n
#
#      n+=1
#      print("second")
#      yield n
#
#      n+=1
#      print("third")
#      yield n
#
# a=my_gen()
# print("next method:")
# # 每次调用a的时候，函数都从之前保存的状态执行
# print(next(a))
# print(next(a))
# print(next(a))
#
# print("for loop:")
# # 与调用next等价的
# b=my_gen()
# for elem in my_gen():
#  print(elem)

#属性方法
# class Foo:
#     def get_bar(self):
#         return 'wupeiqi'
#
#     # *必须两个参数
#     def set_bar(self, value):
#         return 'set value' + value
#
#     def del_bar(self):
#         return 'wupeiqi'
#
#     BAR = property(get_bar, set_bar, del_bar, 'description...')


# obj = Foo()
#
# obj.BAR                  # 自动调用第一个参数中定义的方法：get_bar
# obj.BAR = "alex"         # 自动调用第二个参数中定义的方法：set_bar方法，并将“alex”当作参数传入
# print(obj.BAR.__doc__)   # 自动获取第四个参数中设置的值：description...
# del Foo.BAR              # 自动调用第三个参数中定义的方法：del_bar方法
# from math import log
# import numpy as np
# def KLD(p,q):
#     p,q=zip(*filter(lambda x,y: x!=0 or y!=0, zip(p,q))) #去掉二者都是0的概率值
#     p=p+np.spacing(1)
#     q=q+np.spacing(1)
#     print (p,q)
#     return sum([_p * log(_p/_q,2) for (_p,_q) in zip(p,q)])
# p=[1,2,3,1,2,1,3,1,3,4,1,2,3,1,3,4,1,2,3,1,2,1,2]
# q=[1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,4,1,0,0,0,0,0,0]
# print(KLD(p,q))
# def soulution(p,q):
#     dict1 = {}
#     for key in p:
#         dict1[key] = dict1.get( key, 0 ) + 1
#     dict2 = {}
#     for key in q:
#         dict2[key] = dict2.get( key, 0 ) + 1

# def inputList():
#     p = input("p的分布：")
#     q = input("q的分布：")
#     listq = q.split(' ')
#     listp = p.split(' ')
#     listpp=[ int(i) for i in listp ]
#     listqq=[ int(i) for i in listq ]
#     so( listpp,listqq )
#
# import numpy as np
# def so(p,q):
#     p1 = []
#     q1 = []
#     print( len( p ) )
#
#     def all_list( arr, a ):
#         result = {}
#         for i in set( arr ):
#             result[i] = arr.count( i ) / len( arr )
#             a.append( result[i] )
#         return a
#
#     print( all_list( p, p1 ) )
#     print( all_list( q, q1 ) )
#     A = np.array( all_list( p, p1 ) )
#     B = np.array( all_list( q, q1 ) )
#     print(A/B)
#     def f( t ):
#         return t * np.log( t )
#
#     # 方法一：根据公式求解
#     f1 = np.sum( B * f( A / B ) )
#     print( f1 )
# inputList()

def romanToInt( s ):
    """
    :type s: str
    :rtype: int
    """
    length = len( s ) - 1
    dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    cur = 0
    next = 0
    for i in range( 0, length ):

        cur = dict[s[i]]
        next = dict[s[i + 1]]
        if cur >= next:
            result += cur
        else:
            result -= cur

    result += dict[s[length]]

    return result
print(romanToInt("III"))
