# -*- coding: utf-8 -*-
#解码
from sockjs.tornado import SockJSRouter
from app.views.views_regist import RegistHandler as regist
from app.views.views_chat import ChatHandler as chat
from app.views.views_login import LoginHandler as login
from app.views.views_userprofile import UserprofileHandler as userprofile
from app.views.views_logout import LogoutHandler as logout
from app.views.views_upload import UploadHandler as upload
from app.views.views_chatroom import ChatRoomHandler as chatroom
from app.views.views_msg import MSGHandler as msg
#将视图和映射结合起来
# 路由视图映射：(路由地址,视图)
urls=[
    (r"/regist/",regist),
    (r"/",chat),
    (r"/login/",login),
    (r"/userprofile/",userprofile),
    (r"/logout/",logout),
    (r"/upload/",upload),
    (r"/msg/",msg)
]+ SockJSRouter(chatroom, "/chatroom").urls