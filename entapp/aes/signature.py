# -*- coding: utf-8 -*-

"""
回调签名生成工具
"""

import hashlib

from entapp.utils import *


def generate_signature(token, timestamp, nonce, encrypt):

    """
    从SHA1算法生成安全签名
    :param token: 企业应用回调token
    :param timestamp: 回调时间戳（从URL参数取）
    :param nonce: 回调随机字符串（从URL参数取）
    :param encrypt: 回调json数据的密文字段
    :return: 安全签名

    :type token: str
    :type timestamp: str
    :type nonce: str
    :type encrypt: str
    :rtype: str
    """
    check_type(token, str)
    check_type(timestamp, str)
    check_type(nonce, str)
    check_type(encrypt, str)

    sort_list = [token, timestamp, nonce, encrypt]
    sort_list.sort()
    sha = hashlib.sha1()
    sha.update(bytestr("".join(sort_list)))
    return sha.hexdigest()
