# -*- coding: UTF-8 -*-
'''
@Project ：backend
@File    ：views.py
@Author  ：Yunzhong Luo
@Date    ：2020/12/15 1:04 上午
'''

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.db.models import Q, F, Avg, Min, Sum, Max, Count, FloatField
from django.db.models.functions import Cast
import json
from django.db import connection
from .search import Search
from .Util.userParam import UserParam
from .Util.loginCheck import LoginCheck

def login(request):
    if request.method == 'POST':
        userID = request.POST['id']
        password = request.POST['password']
        # Process the ID to Prevent SQL injection
        userID = LoginCheck.convert(userID)
        if len(userID) == 0:
            print('false')
            #TODO: return false
        # Find if it is in DataBase
        search = Search()
        res = search.loginSearch(userID)
        if len(res) == 0:
            return JsonResponse(0, safe=False, json_dumps_params={'ensure_ascii': False})
        realPass = res[0][0]
        level = 0
        # Check if Equal
        if str(realPass) == str(password):
            # check the level
            level = {'level': res[0][1], 'id': res[0][2]}
        return JsonResponse(level, safe=False, json_dumps_params={'ensure_ascii': False})

def userEnter(request):
    if request.method == 'GET':
        search = Search()
        obj = search.allInfo()
        return JsonResponse(obj, safe=False, json_dumps_params={'ensure_ascii': False})

def userSearch(request):
    if request.method == 'POST':
        # Get Data
        reqData = json.loads(request.body)
        # Get Empty Dictionary
        load = UserParam(reqData)
        emptyDic = load.checkEmpty()
        search = Search()
        obj = search.userSearch(reqData, emptyDic)
        return JsonResponse(obj, safe=False, json_dumps_params={'ensure_ascii': False})

def hostSearch(request):
    if request.method == 'GET':
        # Get Data
        id = request.GET['id']
        search = Search()
        obj = search.hostSearch(id)
        return JsonResponse(obj, safe=False, json_dumps_params={'ensure_ascii': False})

def hostUpdate(request):
    if request.method == 'POST':
        # Get Data
        reqData = json.loads(request.body)
        id = reqData['id']
        name = reqData['name']
        intro = reqData['introduction']
        search = Search()
        try:
            search.hostUpdate(id, name, intro)
            return HttpResponse('Ok')
        except Exception as e:
            print(e)
            return HttpResponse('Fail')


def test(request):
    if request.method == 'POST':
        reqData = json.loads(request.body)
        # Get Empty Dictionary
        print(reqData)
        return HttpResponse('yes')

