# -*- coding: utf-8 -*-
import tornado.web
from app.models.crud import CRUD
from app.params import data as cdata

class CommonHandler(tornado.web.RequestHandler):
    @property
    def params(self):
        data = self.request.arguments
        data = {
            k: list(map(lambda val: str(val, encoding="utf-8"),v))
            for k, v in data.items()
        }
        return data

    @property
    def name(self):
        return self.get_secure_cookie("name",None)

    # 返回用户信息
    @property
    def user(self):
       return CRUD.user(self.name)

    # 公共参数
    @property
    def common_data(self):
        return cdata