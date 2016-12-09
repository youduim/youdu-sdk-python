# -*- coding: utf-8 -*-

"""
回调模式示例，简单企业应用示例
!!需要用python3.5运行!!
"""


from aiohttp import web
from urllib.parse import parse_qsl

import entapp.client as app
from entapp.message import *
from entapp.aes import AESCrypto
from entapp.aes import generate_signature
from entapp.utils import *


BUIN = 0  # 请填写企业总计号

APP_ID = ''  # 请填写企业应用AppId

CALLBACK_AES_KEY = ''  # 请填写企业应用回调AESKey

TOKEN = ''  # 请填写企业应用回调Token

AES_KEY = ''  # 请填写企业应用EncodingAesKey

ADDRESS = '127.0.0.1:7080'  # 请填写有度服务器地址

OUT_DIR = ''  # 请填写测试下载输出目录

# 回调接口
CB_RECEIVE_MSG = '/msg/receive'  # 请填写回调测试接口URI


client = app.AppClient(BUIN, APP_ID, AES_KEY, ADDRESS)


# 接收消息的handler
async def receive_msg(req):
    print(req.path)
    query_dict = dict(parse_qsl(req.query_string))
    signature = query_dict.get('msg_signature')
    if not is_instance(signature, unicode_str(), str):
        print('msg_signature is invalid')
        return

    nonce = query_dict.get('nonce')
    if not is_instance(nonce, unicode_str(), str):
        print('nonce is invalid')
        return

    timestamp = query_dict.get('timestamp')
    if not is_instance(timestamp, unicode_str(), str):
        print('timestamp is invalid')
        return

    json_obj = None
    try:
        json_obj = await req.json()
    except ValueError as e:
        print('failed to decode json', e)
        return

    encrypt = json_obj.get('encrypt')
    if not is_instance(encrypt, unicode_str(), str):
        print('encrypt content is invalid')
        return

    my_signature = generate_signature(TOKEN, timestamp, nonce, encrypt)
    if pystr(signature) != my_signature:
        print('signature not match')
        return

    to_buin = json_obj.get('toBuin')
    if not isinstance(to_buin, int):
        print('toBuin is invalid')
        return

    to_app = json_obj.get('toApp')
    if not is_instance(to_app, unicode_str(), str):
        print('toApp is invalid')
        return

    if to_buin != BUIN or to_app != APP_ID:
        print('buin or appId not match')
        return

    msg_dict = json_loads_utf8(pystr(AESCrypto(APP_ID, CALLBACK_AES_KEY).decrypt(encrypt)))
    msg = ReceiveMessage().from_json_object(msg_dict)
    print(str(msg))

    if msg.msg_type == MESSAGE_TYPE_IMAGE:
        client.download_file(msg.msg_body.to_image_body().media_id, OUT_DIR)
    elif msg.msg_type == MESSAGE_TYPE_FILE:
        client.download_file(msg.msg_body.to_file_body().media_id, OUT_DIR)
    else:
        pass

    return web.Response(text=msg.package_id)


# 创建服务
def init_server():
    app = web.Application()
    app.router.add_post(CB_RECEIVE_MSG, receive_msg)
    return app


# 启动服务
web.run_app(init_server(), port=8080)
