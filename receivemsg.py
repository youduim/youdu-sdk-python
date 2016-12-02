# -*- coding: utf-8 -*-

'''
接收消息示例
'''

from aiohttp import web

import ydapi
from urllib.parse import parse_qsl

# 回调接口
CB_RECEIVE_MSG = '/msg/receive'


# 接收消息的handler
async def receive_msg(req):
    print(req.path)
    querydict = dict(parse_qsl(req.query_string))
    signature = querydict['msg_signature']
    nonce = querydict['nonce']
    timestamp = querydict['timestamp']
    jsonobj = await req.json()
    mysignature = ydapi.get_sha1(ydapi.TOKEN, timestamp, nonce, jsonobj['encrypt'])
    if signature != mysignature:
        print('signature not match')
        return

    msg = ydapi.parse_receive_msg(jsonobj)
    print(msg)
    return web.Response(text=str(msg.packageid))


# 创建服务
def init_server():
    app = web.Application()
    app.router.add_post(CB_RECEIVE_MSG, receive_msg)
    return app


# 启动服务
web.run_app(init_server())
