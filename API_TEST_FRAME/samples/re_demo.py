#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: re_demo.py
# @time: 2020/7/14 22:25
# @desc:  正表达式
import re
# compile(patter):  创建模式对象
# pat =re.compile('A')
# m = pat.search('CBD')
# print(m)
#
# a = re.search('asd','ABCDasd')
# print(a)
# b = re.search('asd','ABCDASD')
# print(b)
#
# pat = re.compile('a')
# print(pat.match('Aasd'))
# print(pat.match('aASD'))
#
# print(re.split(',','a,s,d,asd'))
# print(re.split('[, ]','a , s ,d   ,,,,,asd',maxsplit=2))
#
# patt = re.compile('a')
# print(patt.findall('ASDaDFGAa'))
# print(re.findall('D(.+?)D','ASDaDFGAa'))
#
# pate = re.compile('[A-Z]+')
# print(pate.findall('ASDcDFGAaFFE'))
# patee = re.compile('[A-Z]')
# print(patee.findall('ASDcDFGAa'))
#
# par = re.compile('[A-Za-z]')
# print(par.findall('ASDcEFGAa'))
# par =re.compile('[A-Za-z]+')
# print(par.findall('ASDcEFGAa'))

# re.sub('a','A','asdBBafr')
# print(re.sub('a','A','asdBBafr'))
#
# pattern = re.compile('a')
# print(pattern.sub('A','AAACCCaaaCCCaaaCCCbbbAAA'))
#
# pat = re.compile(r'www\.(.*)\..{3}')
#
# print(pat.match('www.dxy.com').group(1))
#
# par = re.compile(r'(\w+) (\w+)')
# s= 'hello world ! hello hz !'
# print(par.findall(s))
#
# print(re.escape('www.dxy.com'))
#
# pat  = re.compile(r'www\.(.*)\.(.*)')
# m = pat.match('www.dxy.com')
# print(m.group(1))
# print(m.start(2))
# print(m.end(1))
# print(m.span(2))
#
# pat = re.compile('.')
# print(pat.match('abc').group())
# print(pat.search('abc').group())
# print(pat.search(r'\n').group())

# patt = re.compile('\.')
# print(patt.search('abc.efg').group())
#
# print(patt.findall('abc.efg'))
#
# pat = re.compile('[abc]')
# print(pat.match('axbycz').group())
#
# print(pat.search('axbycz').group())
# print(pat.findall('axbycz'))
#
# pat = re.compile('\d')
# print(pat.search('ax1by2cz3').group())
# # print(pat.match('ax1by2cz3').group())
#
# pat1 = re.compile('\D')
# # print(pat1.match('22AAADDD23233').group())
# print(pat1.search('222aaaa222ddd').group())
# print(pat1.findall('222aaa222ccc222ddd'))
# print(pat1.findall('222aaa222ccc222ddd')[0:4])
#
# pat = re.compile('\s')
# pr = re.compile('\S')
#
# print(pat.findall('\rax1 \nxb2  \tcz3'))
# print(pr.findall('\rax1 \nxb2  \tcz3'))
#
#
# prr = re.compile('\w')
# print(prr.match('1a2b3c').group())
# print(prr.search('a1b2c3').group())
# print(prr.findall('aaa22cc33??'))

# par = re.compile('[abc]*')
# print(par.match('abcabcdefabc').group())
# print(par.search('abcabcdefabc').group())
# print(par.findall('abcabcdefabc'))

# par = re.compile('[abc]+')
# print(par.match('abcabcdefabc').group())
# print(par.search('abcabcdefabc').group())
# print(par.findall('abcabcdefabc'))

# par = re.compile('[abc]+')
# print(par.match('abcdefabcabc').group())
# print(par.search('abcdefabcabc').group())
# print(par.findall('abcdefabcabc'))
#
# pat = re.compile('[abc]+?')
# print(pat.match('abcdefabcabc').group())
# print(pat.search('dbbabcdefabcabc').group())
# print(pat.findall('abcdefabcabc'))

# pat = re.compile('[op]{2}')
# print(pat.search('abcooapp').group())
# print(pat.findall('abbcooappp'))

# pat =re.compile('[op]{2,4}')
# print(pat.match('pppabcooapp').group())
# print(pat.search('pppabcooapp').group())
# print(pat.findall('pppabcooapp'))

# pat =re.compile('^[abc]')
# # print(pat.search('defabc').group())
# # print(pat.match('defabc').group())
# print(pat.findall('defabc'))

# pat = re.compile('^[abc]+') #开头中任意一个或者多次，贪婪：匹配多个
# print(pat.findall('cbadefab'))  #  ^  匹配字符串行头或开头

# pat = re.compile(r'^[abc]+?') #开头是a、b、c中的任意一个或多个，非贪婪：匹配一个就停止
# print(pat.findall('aacbadefab'))

# pat = re.compile('[abc]$')
# print(pat.match('adefAbc').group())
# print(pat.search('adefAbc').group())

# pat = re.compile('[abc]+$')
# print(pat.search('adefAbc').group())
# print(pat.findall('adefAbc'))

# pat = re.compile('\A[abc]+')
# print(pat.findall('cbadefab'))
# print(pat.search('cbadefab').group())

# pat = re.compile('[abc]+\Z')
# print(pat.search('cbadefab').group())
# print(pat.findall('cbadefab'))
# pat =re.compile(r'(a)\w(c)')
# print(pat.match('abcdef').group())

# pat = re.compile('(a)b(c)')
# print(pat.match('abcdef').group())
# print(pat.match('abcdef').group(1))
# print(pat.match('abcdef').group(2))

# pat = re.compile(r'www\.(.*)\..{3}')
# print(pat.match('www.dxy.com').group(1))

# pat = re.compile(r'(?P<k>a)\w(c)')
# print(pat.search('abcdef').group())
# print(pat.search('abcdef').group(1))
# print(pat.search('abcdef').group(2))
# print(pat.search('abcdef').groupdict())

pat = re.compile(r'(?P<k>a)\w(c)(?P=k)')
print(pat.search('abcadef').group())
