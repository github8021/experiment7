# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :experiment7
# @File     :text1
# @Date     :2020/10/13 21:03
# @Author   :施嘉伟
# @Email    :1138128021@qq.com
# @Software :PyCharm
-------------------------------------------------
"""
def add(a,b):
    return a+b;

def subtraction(a,b):
    return a-b;

def multiplication(a,b):
    return a*b;

def division(a,b):
    return a/b;

first_number=float(input("请输入第一个数:"))
second_number=float(input("请输入第二个数:"))
operator_type=str(input("请选择要执行的运算符：+、-、*、/:"))
if(operator_type=='+'):
    print("计算结果为{}".format(add(first_number,second_number)))
elif(operator_type=='-'):
    print("计算结果为{}".format(subtraction(first_number,second_number)))
elif(operator_type=='*'):
    print("计算结果为{}".format(multiplication(first_number,second_number)))
elif(operator_type=='/'):
    print("计算结果为{}".format(division(first_number,second_number)))
