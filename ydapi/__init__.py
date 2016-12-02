# -*- coding: utf-8 -*-

'''
有度应用会话接口
'''

from .auth import get_token

from .msg import MSGTYPE_TEXT
from .msg import MSGTYPE_IMG
from .msg import MSGTYPE_FILE
from .msg import MSGTYPE_MPNEWS
from .msg import MSGTYPE_EXLINK
from .msg import Message
from .msg import TextBody
from .msg import ImageBody
from .msg import FileBody
from .msg import MpnewsBody
from .msg import MpnewsBodyCell
from .msg import ExlinkBody
from .msg import ExlinkBodyCell
from .msg import send_msg

from .res import FILETYPE_FILE
from .res import FILETYPE_IMAGE
from .res import upload_file
from .res import download_file

from .receive import REMSGTYPE_TEXT
from .receive import REMSGTYPE_IMAGE
from .receive import REMSGTYPE_FILE
from .receive import ReceiveMessage
from .receive import ReTextBody
from .receive import ReImageBody
from .receive import ReFileBody
from .receive import parse_receive_msg
from .receive import get_sha1

from .const import *

