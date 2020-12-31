# -*- coding: UTF-8 -*-
'''
@Project ：backend 
@File    ：loginCheck.py
@Author  ：Yunzhong Luo 
@Date    ：2020/12/18 10:59 上午 
'''

class LoginCheck:
    @classmethod
    def convert(cls, account):
        illegal = ['<script>', '</script>', '\'', '\"', ' ', '(', ')']
        for item in illegal:
            account = account.replace(item, '')
        return account



