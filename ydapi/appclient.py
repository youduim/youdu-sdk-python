# -*- coding: utf-8 -*-

'''
客户端接口
'''

class AppClient(object):
    '''
    客户端
    '''

    def __init__(self, addr, buin, appid, appkey):
        self.__addr = addr
        self.__buin = buin
        self.__appid = appid
        self.__appkey = appkey

