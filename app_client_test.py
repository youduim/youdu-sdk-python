# -*- coding: utf-8 -*-

"""
主动调用接口测试用例
"""

import unittest

import entapp.client as app
from entapp.message import *


BUIN = 0  # 请填写企业总计号

AES_KEY = ''  # 请填写企业应用EncodingAesKey

APP_ID = ''  # 请填写企业应用AppId

ADDRESS = '127.0.0.1:7080'  # 请填写有度服务器地址

IMAGE_NAME = ''  # 请填写测试图片名称
IMAGE_PATH = ''  # 请填写测试图片路径

FILE_NAME = ''  # 请填写测试文件名称
FILE_PATH = ''  # 请填写测试文件路径

OUT_DIR = ''  # 请填写测试下载输出目录

TO_USER = 'hunter'  # 请填写测试接收消息的账号，使用'|'符号分割

client = app.AppClient(BUIN, APP_ID, AES_KEY, ADDRESS)


class AppClientTestCase(unittest.TestCase):

    def test_send_text_msg(self):
        """
        测试文字消息
        """
        body = TextBody('你好有度')
        msg = Message(TO_USER, MESSAGE_TYPE_TEXT, body)
        client.send_msg(msg)

    def test_send_image_msg(self):
        """
        测试图片消息
        """
        media_id = client.upload_file(app.FILE_TYPE_IMAGE, IMAGE_NAME, IMAGE_PATH)
        body = ImageBody(media_id)
        msg = Message(TO_USER, MESSAGE_TYPE_IMAGE, body)
        client.send_msg(msg)

    def test_send_file_msg(self):
        """
        测试文件消息
        """
        media_id = client.upload_file(app.FILE_TYPE_FILE, FILE_NAME, FILE_PATH)
        body = FileBody(media_id)
        msg = Message(TO_USER, MESSAGE_TYPE_FILE, body)
        client.send_msg(msg)

    def test_send_mpnews_msg(self):
        """
        测试图文消息
        """
        media_id = client.upload_file(app.FILE_TYPE_IMAGE, IMAGE_NAME, IMAGE_PATH)
        body = MpnewsBody([MpnewsBodyCell('你好有度', media_id, '有度', '工作需要张弛有度')])
        msg = Message(TO_USER, MESSAGE_TYPE_MPNEWS, body)
        client.send_msg(msg)

    def test_send_exlink_msg(self):
        """
        测试外链消息
        """
        media_id = client.upload_file(app.FILE_TYPE_IMAGE, IMAGE_NAME, IMAGE_PATH)
        body = ExlinkBody([ExlinkBodyCell('你好有度', 'https://youdu.im', '有度', media_id)])
        msg = Message(TO_USER, MESSAGE_TYPE_EXLINK, body)
        client.send_msg(msg)

    def test_download_image(self):
        """
        测试下载图片
        """
        media_id = client.upload_file(app.FILE_TYPE_IMAGE, IMAGE_NAME, IMAGE_PATH)
        client.download_file(media_id, OUT_DIR)

    def test_download_file(self):
        """
        测试下载文件
        """
        media_id = client.upload_file(app.FILE_TYPE_FILE, FILE_NAME, FILE_PATH)
        client.download_file(media_id, OUT_DIR)

    def test_search_file(self):
        """
        测试搜索文件
        """
        media_id = client.upload_file(app.FILE_TYPE_FILE, FILE_NAME, FILE_PATH)
        exists = client.search_file(media_id)
        self.assertTrue(exists)


if __name__ == '__main__':
    unittest.main()
