#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
# import re
# # m = re.match(r'\d','123abc456')
# # print(m.group())
# #
# # print(re.sub( 'a','A','abcdcasd' ))
# #
# # pat = re.compile('a')
# #
# # print(pat.sub('A','acsaa'))
# # print(re.split(',','a,s,d,asd'))
# # print( re.sub('a','AAA','abcabc') )
# #
# # partten = re.compile( r'www\.(.*)\..{3}' )
# # print(partten.match('www.dxy.com').group(1))
# m=re.findall('aa','aaab')
# print(m)
# print()
import requests
import re
content = requests.get('https://movie.douban.com/chart').text
print(content)
# 豆瓣电影排行榜
pattern = re.compile('class="pl2".*?<.*?="(.*?)".*?>(.*?)<span.*?>(.*?)</span>.*?"rating_nums">(.*?)</span>.*?"pl">(.*?)</span>', re.S)
# compile可以在多次使用中提高效率，这里影响不大
results = re.findall(pattern, content)
for result in results:
    url, name1, name2, nums, pl = result
    print(url, name1.replace("/","").strip(), name2.replace("/","").strip(), nums, pl)
