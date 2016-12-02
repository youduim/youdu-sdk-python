# -*- coding: utf-8 -*-

'''
消息接收回调
'''

from __future__ import print_function

import json
import hashlib

from .const import *
from .helper import *

REMSGTYPE_TEXT = 'text'
REMSGTYPE_IMAGE = 'image'
REMSGTYPE_FILE = 'file'


class ReceiveMessage(object):
    '''
    接收消息类型
    '''

    def __init__(self, jsonobj):
        self.fromuser = jsonobj['fromUser']
        self.createtime = jsonobj['createTime']
        self.packageid = jsonobj['packageId']
        self.msgtype = jsonobj['msgType']
        body = jsonobj[self.msgtype]
        if self.msgtype == REMSGTYPE_TEXT:
            self.msgbody = ReTextBody(body)
        elif self.msgtype == REMSGTYPE_IMAGE:
            self.msgbody = ReImageBody(body)
        elif self.msgbody == REMSGTYPE_FILE:
            self.msgbody = ReFileBody(body)
        else:
            raise Exception('unknown msg type')

    def __str__(self):
        return '(ReMessage {fromuser} {createtime} {packageid} {msgtype} {msgbody})'.format(
            fromuser=self.fromuser, createtime=self.createtime,
            packageid=self.packageid, msgtype=self.msgtype, msgbody=self.msgbody)


class ReTextBody(object):
    '''
    文本消息
    '''

    def __init__(self, jsonobj):
        self.content = jsonobj['content']

    def __str__(self):
        return '(ReTextBody {content})'.format(content=self.content)


class ReImageBody(object):
    '''
    图片消息
    '''

    def __init__(self, jsonobj):
        self.mediaid = jsonobj['media_id']

    def __str__(self):
        return '(ReImageBody {mediaid})'.format(mediaid=self.mediaid)


class ReFileBody(object):
    '''
    文件消息
    '''

    def __init__(self, jsonobj):
        self.mediaid = jsonobj['media_id']

    def __str__(self):
        return '(ReFileBody {mediaid})'.format(mediaid=self.mediaid)


def parse_receive_msg(jsonobj):
    '''
    解析回调返回的json对象
    @param jsonobj: 回调发来的json对象 :type dict
    @return ReMesasge对象
    '''
    if jsonobj['toBuin'] != BUIN:
        raise Exception('buin is not matched')

    if jsonobj['toApp'] != APPID:
        raise Exception('AppID is not matched')

    ciphermsg = jsonobj['encrypt']
    msgdict = json.loads(decrypt(CBKEY, APPID, ciphermsg))
    return ReceiveMessage(msgdict)


def get_sha1(token, timestamp, nonce, encrypt):
    '''
    从SHA1算法生成安全签名
    @param token: 企业应用回调token
    @param timestamp: 回调时间戳（从URL参数取）
    @param nonce: 回调时间戳（从URL参数取）
    @param encrypt: 回调json数据的密文字段
    @return 安全签名
    '''
    sortlist = [token, timestamp, nonce, encrypt]
    sortlist.sort()
    sha = hashlib.sha1()
    sha.update(bytestr("".join(sortlist)))
    return sha.hexdigest()
    