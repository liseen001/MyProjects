#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:
import paramiko
from pymysql import connect,cursors

def connetc_linux():
    # try:
        #建立一个sshclient对象
        ssh = paramiko.SSHClient()
        #允许将信任的主机自动加入到host_allow 列表，此方法必须放在connect方法的前面
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #调用connect方法连接服务器
        ssh.connect(hostname="192.168.101.107",port=22,username='root',password='Aa123456')
        #执行命令
        stdin,stdout,stderr = ssh.exec_command('cd /datas/txv3.0/tx-api-merge2/logs')
        result = stdout.read(65533)
        #关闭linux连接
        ssh.close()
        return result


if __name__=="__main__":
    print(connetc_linux())