# -*- coding: utf-8 -*-

"""
类型相关工具
"""


def check_type(value, value_type):
    """
    检查变量类型是否匹配，不匹配则抛出TypeError
    :param value: 变量
    :param value_type: 类型

    :type value: object
    :type value_type: cls
    """
    if not isinstance(value, value_type):
        raise TypeError('the value does not match type {var_type}'.format(var_type=value_type))
