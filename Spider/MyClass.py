# coding=utf-8
# 定义类
class MyClass:
    # 定义方法
    def myMethod(self):
        print 'HelloWorld' # 方法体
    def plus(self):
        a1 = 1
        a2 = 2
        a3 = 3
        total1 = a1 + a2 + a3
        total2 = a1 + \
                 a2 + \
                 a3
        print total1,total2
mc = MyClass() # 创建对象
mc.myMethod() # 调用方法
mc.plus()