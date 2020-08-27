#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import os
from faker import Faker

class FakerTest():
    def __init__(self):
        self.__faker = Faker(locale='zh_CN')

    @property
    def create_random_country_code(self):
        '''生成随机国家编码'''
        return self.__faker.country_code()

    @property
    def create_random_address(self):
        '''生成随机地址'''
        return '中华人民共和国'+self.__faker.address()

    @property
    def create_random_name(self):
        '''生成随机姓名'''
        return self.__faker.name()

    @property
    def create_numerify(self):
        '''生成随机的三位数字'''
        return self.__faker.numerify()
    @property
    def create_random_digit(self):
        '''随机生成0-9中的一个数字'''
        return self.__faker.random_digit()

    @property
    def create_random_digit_not_null(self):
        '''随机生成1-9中的一个数字'''
        return self.__faker.random_digit_not_null()

    @property
    def create_random_int(self):
        '''指定范围内生成随机整数'''
        return self.__faker.random_int(0,100000)

    @property
    def create_random_number(self):
        '''随机生成指定长度的数字'''
        return self.__faker.random_number(5)

    @property
    def create_random_element(self):
        '''随机生成小写英文字母'''
        return self.__faker.random_element()

    @property
    def create_random_letter(self):
        '''随机生成大写英文字母'''
        return self.__faker.random_letter()

    @property
    def create_color_name(self):
        '''随机生成颜色名'''
        return self.__faker.color_name()

    @property
    def create_bs(self):
        '''随机生成公司服务名'''
        return self.__faker.bs()

    @property
    def create_company_name(self):
        '''随机生成长名字公司名'''
        return self.__faker.company()

    @property
    def create_credit_card_expire(self):
        '''随机生成信用卡到期日'''
        return self.__faker.credit_card_expire()

    @property
    def create_credit_card_full(self):
        '''随机生成完整信用卡信息'''
        return self.__faker.credit_card_full()

    @property
    def create_credit_card_number(self):
        '''随机生成信用卡号'''
        return self.__faker.credit_card_number()

    @property
    def create_credit_card_provider(self):
        '''随机生成信用卡类型'''
        return self.__faker.credit_card_provider()

    @property
    def create_credit_card_security_code(self):
        '''随机生成信用卡安全码'''
        return self.__faker.credit_card_security_code()

    @property
    def create_random_date(self):
        '''随机生成日期'''
        return self.__faker.date()

    @property
    def create_randon_ssn(self):
        '''随机生成身份证'''
        return self.__faker.ssn()

    @property
    def create_random_chrome(self):
        '''随机生成谷歌uder_agent信息'''
        return self.__faker.chrome()

faker = FakerTest()

if __name__ == '__main__':
    print( FakerTest().create_random_chrome)
