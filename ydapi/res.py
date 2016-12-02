# -*- coding: utf-8 -*-

'''
文件上传下载相关
'''

from __future__ import print_function

import json
from os.path import join, abspath

import requests
from requests_toolbelt import MultipartEncoder

from .const import *
from .helper import *

FILETYPE_FILE = 'file'
FILETYPE_IMAGE = 'image'


def upload_file(token, ftype, fname, fpath):
    '''
    上传文件接口
    @param ftype: 文件类型 :type str
    @param fname: 文件名字 :type str
    @param fpath: 文件路径 :type str
    @return media id :type str
    '''
    ciphername = encrypt(APPKEY, APPID, json.dumps({'type':ftype, 'name': fname}))
    encryptfile = ''
    with open(fpath, 'rb') as file:
        encryptfile = encrypt(APPKEY, APPID, file.read())

    encoder = MultipartEncoder(
        fields={'encrypt': ciphername,
                'file': ('file', encryptfile, 'text/plain')}
    )

    req = requests.post(API_UPLOAD_FILE + '?accessToken={token}'.format(token=token), data=encoder,
                        headers={'Content-Type': encoder.content_type})
    parse_status(req)
    parse_err(req.json())
    cipherid = req.json()['encrypt']
    return json.loads(decrypt(APPKEY, APPID, cipherid))['mediaId']


def download_file(token, ftype, mediaid, fpath):
    '''
    下载文件接口
    @param ftype: 文件类型 :type str
    @param mediaid: media id :type str
    @param fpath: 保存文件路径
    @return (name: 文件名称, size: 文件大小) :type (str, int)
    '''
    cipherid = encrypt(APPKEY, APPID, json.dumps(
        {'type': ftype, 'mediaId': mediaid}))
    param = {'buin': BUIN, 'encrypt': cipherid}
    req = requests.post(API_DOWNLOAD_FILE +
                        '?accessToken={token}'.format(token=token), json=param)
    parse_status(req)
    jsonret = {'errcode':0, 'errmsg': ''}
    try:
        jsonret = req.json()
    except Exception:
        pass
    parse_err(jsonret)
    cipherinfo = req.headers.get('encrypt')
    if cipherinfo is None:
        raise Exception('no file info received')

    fileinfo = json.loads(decrypt(APPKEY, APPID, cipherinfo))
    filename = fileinfo['name']
    filesize = fileinfo['size']
    with open(abspath(join(fpath, filename)), 'wb') as file:
        file.write(decrypt_file(APPKEY, APPID, req.content))

    return (filename, filesize)
