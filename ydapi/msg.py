# -*- coding: utf-8 -*-

'''
消息发送
'''

from __future__ import print_function

import json

import requests

from .const import *
from .helper import *

MSGTYPE_TEXT = 'text'
MSGTYPE_IMG = 'image'
MSGTYPE_MPNEWS = 'mpnews'
MSGTYPE_FILE = 'file'
MSGTYPE_EXLINK = 'exlink'


class Message(object):
    '''
    消息结构
    '''

    def __init__(self, touser, msgtype, msgbody):
        self.touser = touser
        self.msgtype = msgtype
        self.msgbody = msgbody

    def json(self):
        return {'toUser': self.touser,
                'msgType': self.msgtype, self.msgtype: self.msgbody.json()}


class TextBody(object):
    '''
    文本消息
    '''

    def __init__(self, content):
        self.content = content

    def json(self):
        return {'content': self.content}


class ImageBody(object):
    '''
    图片消息
    '''

    def __init__(self, mediaid):
        self.mediaid = mediaid

    def json(self):
        return {'media_id': self.mediaid}


class MpnewsBody(object):
    '''
    图文消息
    '''

    def __init__(self, msglist):
        self.msglist = msglist

    def json(self):
        return list(self.msglist)


class MpnewsBodyCell(object):
    '''
    图文消息cell
    '''

    def __init__(self, title, mediaid, digest, content):
        self.title = title
        self.mediaid = mediaid
        self.digest = digest
        self.content = content

    def json(self):
        return {'title': self.title, 'media_id': self.mediaid, 'digest': self.digest, 'content': self.content}


class FileBody(object):
    '''
    文件消息
    '''

    def __init__(self, mediaid):
        self.mediaid = mediaid

    def json(self):
        return {'media_id': self.mediaid}


class ExlinkBody(object):
    '''
    外链消息
    '''
    def __init__(self, msglist):
        self.msglist = msglist

    def json(self):
        return self.msglist

class ExlinkBodyCell(object):
    '''
    外链消息cell
    '''

    def __init__(self, title, url, digest, mediaid):
        self.title = title
        self.url = url
        self.digest = digest
        self.mediaid = mediaid

    def json(self):
        return {'title': self.title, 'url': self.url,
                'digest': self.digest, 'media_id': self.mediaid}


def send_msg(token, msg):
    '''
    发送消息
    @param token: access token :type str
    @param msg: Message对象 :type Message
    @return True
    '''
    ciphertext = encrypt(APPKEY, APPID, json.dumps(msg.json()))
    param = {'buin': BUIN, 'appId': APPID, 'encrypt': ciphertext}
    req = requests.post(
        API_SEND_MSG + '?accessToken={token}'.format(token=token), json=param)
    parse_status(req)
    parse_err(req.json())
    return True
