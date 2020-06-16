#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import hmac,base64,struct,hashlib,time,random


def get_hotp_token(secret,intervals_no):
    key = base64.b32decode(secret,True)
    msg = struct.pack('>Q',intervals_no)
    h = hmac.new(key,msg,hashlib.sha1).digest()
    o = ord(chr(h[19])) & 15
    h = (struct.unpack('>I',h[o:o+4])[0] & 0x7fffffff) % 1000000
    return h
def get_totp_token(secret):
    return get_hotp_token(secret,intervals_no=int(time.time())//30)
'''通过谷歌秘钥获取验证码'''
def get_goole_code():
    secret = 'OAMNRB7WA6HW2PUZ'
    googlecode = get_hotp_token(secret,intervals_no=int(time.time())//30)
    return '%06d' % googlecode

'''随机生成多个count随机整数，随机整数的最大值和最小值'''
def get_randomint(min,max,count=None):
    randomint_list = []
    for i in range(count):
        randomint_list.append(random.randint(min,max))
    return randomint_list
'''顺序取值:最大值、最小值、步长、生成的数量'''
def get_seq_ints(min,max,step=1,count=None):
    randomint_list = list( range(min,max,step) )
    if count:
        return randomint_list[0:count]
    else:
        return randomint_list

'''生成随机字符串，字符串长度为变量,生成多少个字符串,生成的是一个列表'''
def get_str_list(randomlength,count):
    str_list = []
    base_str = 'ABCDEFGHIJKLMNOPKRETUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    length = len(base_str) -1
    for i in range(count):
        ran_str = ''
        for i in range(randomlength):
            ran_str +=base_str[random.randint(0,length)]
        str_list.append(ran_str)
    return str_list
'''生成随机字符串'''
def get_str(randomlength,count):
    base_str = 'ABCDEFGHIJKLMNOPKRETUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    length = len(base_str) -1
    for i in range(count):
        ran_str = ''
        for i in range(randomlength):
            ran_str +=base_str[random.randint(0,length)]
    return ran_str

'''生成随机手机号'''
def get_random_mobilephone(count):
    phone_list = []
    for i in range(count):
        start_phone = random.choice(['130','131','132','133','134','135','136','137','138','139','147',
                                     '153','155','156','157','158','159','186','187','188'])
        end_phone = ''.join(random.sample('0123456789',8))  #join把一个字符列表转换为字符串
        phone_list.append(start_phone+end_phone)
    return phone_list

if __name__=="__main__":
    print(type(get_str(1,2)),get_str(5,2))