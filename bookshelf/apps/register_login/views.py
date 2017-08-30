# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid
import json
import simplejson
import requests

from django.shortcuts import render
from django.http import HttpResponse
import datetime


from .. import untils_
from services import *


def regist(request):
    if request.method == 'GET':
        appid = 'wxaab569c52de78bc3'
        appsecret = 'b1e31005610020ffb5311b5952ff00f6'
        code = request.GET['code']
        get_acces_tooken_url = 'https://api.weixin.qq.com/sns/oauth2/access_token?appid=' + \
                               appid + '&secret=' + appsecret + '&code=' + code + \
                               '&grant_type=authorization_code'
        response = requests.get(get_acces_tooken_url).text
        openid = eval(response)['openid']

        response = HttpResponse("regist")
        response.set_cookie("openid", openid, 72000)
        return response


    id_ = request.COOKIES.get('openid')
    if id_:
        openid = id_

    req = simplejson.loads(request.body)
    password = req.get("password", 0)
    tel = req.get('tel', 0)
    if not password or not tel:
        return HttpResponse('wrong')
    obj = {"password": password,
           "tel_no": tel,
           "open_id": openid,
           "borrow_limit_num": 5,
           "borrow_num": 0,
           "order_num": 0,
           "active_time": datetime.datetime.now()}
    handel_regist(obj)

    return HttpResponse("ok")


def login(request):

    req = simplejson.loads(request.body)
    tel = req.get('tel')
    password = req.get('password')
    if not password or not tel:
        return HttpResponse('wrong')
    obj = {"tel_no": tel,
           "password": password}
    res = handel_login(obj)
    if res:
        response = HttpResponse("ok")
        response.set_cookie("openid", res[0].open_id, 72000)

        return response
    else:

        return HttpResponse("wrong")


def user_center(request):
    openid = request.COOKIES.get('openid', 0)
    if openid:
        return HttpResponse(json.dumps(center_service(openid)))
    else:
        return HttpResponse('login_need')
