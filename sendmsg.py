# -*- coding: utf-8 -*-

'''
发送消息示例
'''

from __future__ import print_function

import sys

import ydapi

# 获取accesstoken
token, expire = ydapi.get_token()
print('token = {token}'.format(token=token))
print('expire = {expire}'.format(expire=expire))

# 上传图片
imgid = ydapi.upload_file(token, ydapi.FILETYPE_IMAGE, '', '')
print('imgid = {imgid}'.format(imgid=imgid))

# 下载图片
ydapi.download_file(token, ydapi.FILETYPE_IMAGE, imgid, '')

# 上传文件
fileid = ydapi.upload_file(token, ydapi.FILETYPE_FILE, '', '')
print('fileid = {fileid}'.format(fileid=fileid))

# 下载文件
ydapi.download_file(token, ydapi.FILETYPE_FILE, fileid, '')

# 发送文本消息
body = ydapi.TextBody("你好有度")
msg = ydapi.Message('hunter', ydapi.MSGTYPE_TEXT, body)
ydapi.send_msg(token, msg)

# 发送图片消息
body = ydapi.ImageBody(imgid)
msg = ydapi.Message('hunter', ydapi.MSGTYPE_IMG, body)
ydapi.send_msg(token, msg)

# 发送图文消息
cell = ydapi.MpnewsBodyCell(
    '你好', imgid, '有度', '工作需要张弛有度')
body = ydapi.MpnewsBody([cell.json()])
msg = ydapi.Message('hunter', ydapi.MSGTYPE_MPNEWS, body)
ydapi.send_msg(token, msg)

# 发送文件消息
body = ydapi.FileBody(fileid)
msg = ydapi.Message('hunter', ydapi.MSGTYPE_FILE, body)
ydapi.send_msg(token, msg)

# 发送外链消息
cell = ydapi.ExlinkBodyCell('你好', 'https://youdu.im', '有度', imgid)
body = ydapi.ExlinkBody([cell.json()])
msg = ydapi.Message('hunter', ydapi.MSGTYPE_EXLINK, body)
ydapi.send_msg(token, msg)
