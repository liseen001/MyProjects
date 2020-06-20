#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo02.py
# @time: 2020/6/6 0:12
# @desc:
'''
1、自动贩卖机：只接受1元，5元、10元的纸币或硬币，最多不超过十块钱，饮料只要橙汁、椰汁、矿泉水、早餐奶、售价分别是3.5、4、2、4.5
写一个函数来标识贩卖机的功能：用户投钱和选择饮料，并判断之后，给用户突出饮料和找零。
说明：参数有一个金额，此金额为输入的总金额
'''

drink_price ={"橙汁":3.5,"椰汁":4,"矿泉水":2,"早餐奶":4.5}

def auto_fanmaiji(money,drink_name):
    if money<=10:
        for drink,price in drink_price.items():
            if drink_name == drink:
                if money > price:
                    print('请取出饮料：%s'%drink_name)
                    print('应找您%3.1f元'%(money-price))
                elif money ==price:
                    print('请取出饮料：%s'%drink_name)
                else:
                    print('sorry,您的余额不足以买：%s'%drink_name)
            else:
                continue
    else:
        print('sorry,本机最大金额不能超过10元，请重试！')

auto_fanmaiji(7.3,"椰汁")