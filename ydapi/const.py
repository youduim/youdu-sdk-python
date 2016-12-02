# -*- coding: utf-8 -*-

'''
常量
'''

SCHEME = 'http://'

URL_YOUDU_API = '127.0.0.1:7080'

API_GET_TOKEN = SCHEME + URL_YOUDU_API + \
    '/v3/api/jgapp/ent.app.accesstoken.gen'

API_SEND_MSG = SCHEME + URL_YOUDU_API + '/v3/api/jgapp/ent.app.msg.send'

API_UPLOAD_FILE = SCHEME + URL_YOUDU_API + '/v3/api/jgapp/ent.app.media.upload'

API_DOWNLOAD_FILE = SCHEME + URL_YOUDU_API + '/v3/api/jgapp/ent.app.media.get'

BUIN = 0

APPKEY = ''

APPID = ''

CBKEY = ''

TOKEN = ''
