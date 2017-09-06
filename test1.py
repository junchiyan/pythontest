#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#------------第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释
#------------第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码

#廖雪松的教程------------------。学习曲线太陡，到中间就不知所谓了，全是没用的东西，不连贯。

#print('hello y')
#print(100+200+300)
#print('jerry','yan')
#print(12.5+22.36)
#print('1024*768=',1024*768)
#------------

#name=input('输入姓名：')
#print('hello,',name)
#------------

#当语句以冒号:结尾时，缩进的语句视为代码块。Python程序是大小写敏感的
#数据类型，整数，浮点数，字符串（转义字符\，加r不转义，多行用''' '''）
#布尔值只有True、False,注意大小写。空是None。变量，常量名全用大写。整除//,求余数%
#UTF-8 可变长度编码。字符串操作，ord(),chr(),字符串前加b表示占用字节，decode(),len(),格式化字符串%d,%f,%s,%x

#list是一个集合,用[]定义，索引从0开始，可用索引[x]访问。可用len()，方法append(),insert(),pop(),元素类型可以不同，元素可以是list。
#tuple元组，用()定义,一旦初始化就不能修改(指向不能修改),没有方法可用索引，只有1个元素的tuple定义时必后边多加一个逗号。元素可以是list

age = 5
if age >= 18:
    print('your age is', age)
    print('adult')
elif age<6:
    print('child')
else:
    print('your age is', age)
    print('teenager')
#--------------------
sum = 0
for x in (1, 2, 3, 4, 10):  #也可以用list
    sum = sum + x
print(sum)
#range()函数,range(5)生成0-4序列，可通过list(range(5))生成[0，1，2，3，4]
#for循环，while循环，break,continue

#dict字典，查找速度快浪费内存。用大括号定义 d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}，通过key：value，查找时用d['Bob']
#get()方法，pop(key),key是不可变对象。

#set是一组key的集合，但不存储value，重复元素在set中自动被过滤

#abs()求绝对值函数，help(abs)查看函数帮助，max(),int(),hex(),都是内置函数。

#定义函数def 函数名(参数名)： 缩进块内写函数体， return返回值，可以返回多个值分别赋给变量实质返回值是tuple元组。pass占位符什么都不做。参数不对会报错。
#位置参数。默认参数在括号内赋初值可简化调用，默认参数必须指向不变对象。可变参数，加星号，可将list或tuple的所有数据传入。
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum # calc(1, 3, 5, 7)将参数组成一个list再for。 nums = [1, 2, 3] 也可用星传递list，calc(*nums)
#关键字参数，用**定义。关键字参数在函数内部自动组装为一个dict。命名关键字参数，用*做分隔符，后面的参数为命名关键字参数限制关键字名字。
#如果之前已经有个一个可变参数，则之后的参数不需要分隔符。5种参数都可以组合使用注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
#默认参数一定要用不可变对象

#递归函数，自己调用自己。利用堆栈，可能会溢出。

#切片 L[0:3] 取list中的0-2索引对应元素，L[-2:-1]取倒数,也可省略某索引。L[:10:2]间隔2。元组tuple和字符串后面接[::2]也可切片。
#迭代 通过for来遍历列表和元组。字典也可按照key或value迭代。
#列表生成式  [x * x for x in range(1, 11)]   [s.lower() for s in L] 使程序简洁。
#生成器 一边循环一边计算的机制，称为生成器：generator  一个列表生成式的[]改成()
#迭代器 ？？？

#函数式编程 允许把函数本身作为参数传入另一个函数，Python对函数式编程提供部分支持。
#函数本身可赋给变量，变量指向该函数。 传入函数，将函数名作为参数传递。
#map()-----, reduce()---,filter()过滤序列。sorted()排序。
#函数作为返回值，函数并未执行。闭包。
#匿名函数lambda
#“装饰器”（Decorator)
#偏函数，----

#模块，一个.py文件就称之为一个模块（Module），为了避免模块名冲突，Python又引入了按目录来组织模块的方法，称为包（Package）
#每一个包目录下面都会有一个__init__.py的文件，任何模块代码的第一个字符串都被视为模块的文档注释。__author__ = 'Michael Liao'作者名字。
#import sys 导入模块。if __name__=='__main__':    test()运行测试。
#作用域 正常的函数和变量名是公开的（public）。类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用

#安装第三方模块，包管理工具pip。命令提示符环境输入 pip install numpy 会自动下载安装合适版本。模块搜索路径，自动搜索也可自定义。

#类（Class）和实例（Instance），对象的方法（Method）。class 类型(继承类)：    类体
#实例名=类名()   。特殊方法“init”前后有两个下划线！！！__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self
#定义一个方法，除了第一个参数是self外，其他和普通函数一样。要调用一个方法，只需要在实例变量上直接调用，除了self不用传递，其他参数正常传入
#访问限制  私有变量
#继承和多态 子类继承父类的方法，覆盖父类方法 多态，Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以
#判断对象类型 type(),isinstance(),获得一个对象的所有属性和方法dir()
#给实例绑定属性的方法是通过实例变量，或者通过self变量.千万不要把实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。

#定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法.给一个实例绑定的方法，对另一个实例是不起作用
##给所有实例都绑定方法，可以给class绑定方法.
#限制实例的属性,定义一个特殊的__slots__变量，来限制该class实例能添加的属性
#Python内置的@property装饰器就是负责把一个方法变成属性调用的,??????????
#多重继承，      MixIn的目的就是给一个类增加多个功能。
#定制类  __str__()，__iter__(),__getitem__()，__getattr__(),__call__()??????????
#枚举类 Enum
#使用元类 type(),metaclass的类名总是以Metaclass结尾

#错误，调试和测试 ？？？？？？？？

#IO编程 同步，异步。文件操作 open(),read(),close(). 二进制模式'rb'，字符编码encoding='gbk'。写write()但是务必要调用f.close()来关闭文件
#StringIO就是在内存中读写str。二进制数据，就需要使用BytesIO。
#操作文件和目录  import os     os.name 后'posix'表示非win'nt'表示win系统。获取详细信息用uname()。在操作系统中定义的环境变量，全部保存在os.environ这个变量中
#操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中
#序列化pickling 把变量从内存中变成可存储或传输的过程称之为序列化 import pickle    pickle.dump(d, f) 读取d = pickle.load(f) 
#序列化为JSON，JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便
# import json     json.dumps(d)     json.loads() JSON编码是UTF-8  类转化为JSON，可先转为dict用__dict__属性再转json

#进程和线程 进程（Process）线程（Thread）一般为多进程或多线程，混合太复杂没用。
#进程
#线程
#ThreadLocal
#在Windows下，多线程的效率比多进程要高，所以微软的IIS服务器默认采用多线程模式。由于多线程存在稳定性的问题，IIS的稳定性就不如Apache。在Thread和Process中，应当优选Process，因为Process更稳定
#分布式进程

#正则表达式

#常用内建模块 datetime    collections     Base64是一种用64个字符来表示任意二进制数据的方法。struct。hashlib。itertools提供了非常有用的用于操作迭代对象的函数。
#contextlib    XML    HTMLParser解析HTML      urllib提供了一系列用于操作URL的功能      
#常用第三方模块 PyPI - the Python Package Index上注册，只要找到对应的模块名字，即可用pip安装        
#图像处理标准库PIL Pillow支持python3.  命令行  pip install pillow。    virtualenv为一个应用创建一套“隔离”的Python运行环境

#图形界面Python自带的库是支持Tk的Tkinter，使用Tkinter，无需安装任何包，就可以直接使用。Python内置的Tkinter可以满足基本的GUI程序的要求，如果是非常复杂的GUI程序，建议用操作系统原生支持的语言和库来编写

#网络编程 我们用一个Socket表示“打开了一个网络链接”，打开一个Socket需要知道目标计算机的IP地址和端口号，再指定协议类型
#TCP编程 客户端....    服务器端....          UDP编程。 电子邮件SMTP，POP3。
#访问数据库  MySQL安装使用。  Python就内置了SQLite3
#web开发 http协议。html,css,JavaScript.    WSGI：Web Server Gateway Interface,Python内置了一个WSGI服务器，这个模块叫wsgiref
#使用Web框架 用Flask编写Web App比WSGI接口简单。MVC：Model-View-Controller，中文名“模型-视图-控制器”有了MVC，我们就分离了Python代码和HTML代码。HTML代码全部放到模板里，写起来更有效率

#异步IO？？？？？？？？

#实战















