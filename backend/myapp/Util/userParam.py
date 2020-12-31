# -*- coding: UTF-8 -*-
'''
@Project ：backend 
@File    ：userParam.py
@Author  ：Yunzhong Luo 
@Date    ：2020/12/17 8:50 下午 
'''

class UserParam:
    def __init__(self, reqData):
        self.data = reqData

    def _isEmpty(self, data):
        if type(data) == 'list':
            return False
        elif type(data) == int and data == 0:
            return False
        elif data == None:
            return False
        else:
            return True

    def checkEmpty(self):
        emptyDic = {}
        for k ,v in self.data.items():
            emptyDic[k] = self._isEmpty(v)
        return emptyDic
