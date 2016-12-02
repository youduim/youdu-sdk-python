# -*- coding: utf-8 -*-

'''
工具函数，包括字符串与字节数组转换、加解密等

关于Crypto.Cipher模块，ImportError: No module named 'Crypto'解决方案
请到官方网站 https://www.dlitz.net/software/pycrypto/ 下载pycrypto。
下载后，按照README中的“Installation”小节的提示进行pycrypto安装。

加解密的示例：

key = base64.b64encode(bytestr('hello'))
appid = 'abcd'
msg = '你好吗'
enmsg = encrypt(key, appid, msg)
print(decrypt(key, appid, enmsg))

'''

from __future__ import print_function

import base64
import struct
from platform import python_version_tuple

import requests
from Crypto import Random
from Crypto.Cipher import AES


def bytestr(text):
    '''
    字符串转字节数组，使用utf-8编码
    @param text: 字符串
    @return 字节数组
    '''
    if int(python_version_tuple()[0]) < 3:
        if isinstance(text, str):
            return text
        else:
            return text.encode(encoding='utf_8')
    else:
        if isinstance(text, str):
            return text.encode(encoding='utf_8', errors='strict')
        else:
            return text


def unistr(text):
    '''
    字节数组转字符串，使用utf-8编码
    @param text: 字节数组
    @return 字符串
    '''
    if int(python_version_tuple()[0]) < 3:
        if isinstance(text, str):
            return text.decode(encoding='utf_8')
        else:
            return text
    else:
        if isinstance(text, str):
            return text
        else:
            return text.decode(encoding='utf_8', errors='strict')

__AES_PADDING__ = 32


def encrypt(key, appid, msg):
    '''
    AES加密
    @param key: 密钥 :type str
    @param appid: 应用的AppID :type str
    @param msg: 内容明文 :type str
    @return  base64后的密文 :type unicode
    '''
    randstr = Random.new().read(16)
    msglen = struct.pack('!i', len(bytestr(msg)))
    paddedkey = struct.pack('{n}s'.format(
        n=__AES_PADDING__), base64.b64decode(key))
    aes = AES.new(paddedkey, mode=AES.MODE_CBC, IV=randstr)
    text = randstr + msglen + bytestr(msg) + bytestr(appid)
    paddedtext = struct.pack('{n}s'.format(
        n=(len(text) // __AES_PADDING__ + 1) * __AES_PADDING__), text)
    paddinglen = __AES_PADDING__ - len(text) % __AES_PADDING__
    paddedtext = paddedtext[0:-paddinglen] + \
        struct.pack('b', paddinglen) * paddinglen
    ciphertext = aes.encrypt(paddedtext)
    return unistr(base64.b64encode(ciphertext))


def __decrypt(key, appid, msg):
    ciphertext = base64.b64decode(msg)
    paddedkey = struct.pack('{n}s'.format(
        n=__AES_PADDING__), base64.b64decode(key))
    randstr = Random.new().read(16)
    aes = AES.new(paddedkey, mode=AES.MODE_CBC, IV=randstr)
    text = aes.decrypt(ciphertext)
    paddinglen = text[len(text) - 1]
    if isinstance(paddinglen, str):
        paddinglen = ord(paddinglen)
    text = text[0:-paddinglen]
    if len(text) <= 20:
        raise Exception('invalid msg')

    msglen = struct.unpack('!i', text[16:20])[0]
    if len(text) <= 20 + msglen:
        raise Exception('invalid msg')

    destappid = text[20 + msglen:]
    if destappid != bytestr(appid):
        raise Exception('unmatched AppID!', unistr(destappid))

    return text[20:20 + msglen]


def decrypt(key, appid, msg):
    '''
    AES解密
    @param key: 密钥 :type str
    @param appid: 应用的AppID :type str
    @param msg: 内容密文 :type str
    @return 解密后的内容 :type unicode
    '''
    return unistr(__decrypt(key, appid, msg))


def decrypt_file(key, appid, content):
    '''
    AES解密文件内容
    @param key: 密钥 :type str
    @param appid: 应用的AppID :type str
    @param content: 内容密文 :type str
    @return 解密后的内容 :type bytestr
    '''
    return bytestr(__decrypt(key, appid, content))


def parse_status(req):
    '''
    解析接口错误码
    @param req: requests返回的请求结果
    @return True
    '''
    if req.status_code != requests.codes.OK:
        req.raise_for_status()

    return True


def parse_err(respjson):
    '''
    解析错误json信息，如果有错误直接抛出异常
    @param respjson: 接口返回的json信息 :type dict
    @return True
    '''
    if respjson['errcode'] != 0:
        raise Exception('error: {code}, {msg}'.format(
            code=respjson['errcode'], msg=respjson['errmsg']))

    return True

