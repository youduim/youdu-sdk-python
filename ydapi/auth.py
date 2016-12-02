# -*- coding: utf-8 -*-

'''
认证相关
'''

from __future__ import print_function

import json
import time

import requests

from .const import *
from .helper import *


def get_token():
    '''
    获取token
    @param buin: 企业总机号 :type int
    @param appid: 企业应用AppId :type str
    @return 企业应用(token, expire) :type (str, int)
    '''
    ciphertext = encrypt(
        APPKEY, APPID, str(int(time.time())))
    param = {'buin': BUIN, 'appId': APPID, 'encrypt': ciphertext}
    req = requests.post(API_GET_TOKEN, json=param)
    parse_status(req)
    parse_err(req.json())
    token = json.loads(decrypt(APPKEY, APPID, req.json()['encrypt']))
    return (token['accessToken'], int(token['expireIn']))
