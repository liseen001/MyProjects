#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: mysql_demo01.py
# @time: 2020/8/13 23:40
# @desc: 连接数据库
import pymysql

connect = pymysql.connect(host='127.0.0.1',
                          port=3306,
                          user='root',
                          password='123456',
                          database='api_test',
                          charset='utf8') #默认字符集

cur = connect.cursor(cursor=pymysql.cursors.DictCursor) #创建游标 以字典形式返回
sql_str='''
select case_info.case_id,case_info.case_name,case_info.is_run,
case_step_info.case_step_name,api_info.api_name,api_info.api_request_type,
api_info.api_request_url,api_info.api_url_params,api_post_data,case_step_info.get_value_type,
case_step_info.variable_name,case_step_info.get_value_code,case_step_info.excepted_result_type,
case_step_info.excepted_result
from case_step_info 
LEFT JOIN case_info on case_step_info.case_id = case_info.case_id
LEFT JOIN api_info on case_step_info.api_id = api_info.api_id 
where case_info.is_run = '是'
order by case_info.case_id,case_step_info.case_step_name;
'''
cur.execute( sql_str )

for i in cur.fetchall():
    print( i )