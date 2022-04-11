# -*- coding: utf-8 -*-
import datetime
import json
from sockjs.tornado import SockJSConnection
from app.models.crud import CRUD

#聊天室视图

class ChatRoomHandler(SockJSConnection):
    waiters = set() #客户端集合

    #1.建立连接
    def on_open(self, request):
        try:
            self.waiters.add(self)
        except Exception as e:
            print(e)
    #全双工通信
    def on_message(self, message):
        # 把信息广播(从服务器推送到所有的客户端)给所有的客户端
        try:
            data = json.loads(message)# 将json字符串反序列为字典以便于标记信息发送时间
            data["dt"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            content = json.dumps(data) # 将字典序列化为json字符串
            if data['code'] == 2:
                CRUD.save_msg(content)
            self.broadcast(self.waiters, content)
        except Exception as e:
            print(e)#打印异常

        # 3.关闭连接
    def on_close(self):
        try:
            self.waiters.add(self)
        except Exception as e:
            print(e)