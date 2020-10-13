# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :experiment7
# @File     :text2
# @Date     :2020/10/13 22:10
# @Author   :施嘉伟
# @Email    :1138128021@qq.com
# @Software :PyCharm
-------------------------------------------------
"""
def fibonacci(n):
    if(n==1 or n==2):
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

sum=0
for i in range(1,31):
    print(fibonacci(i))
    sum+=fibonacci(i)

print("sum={}".format(sum))

