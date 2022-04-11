# -*- coding: utf-8 -*-
import tornado.web
from app.views.views_common import CommonHandler
from app.tools.form import LoginForm
from werkzeug.datastructures import MultiDict

class LoginHandler(CommonHandler):
    def get(self,*args,**kwargs):
        data = dict(
            title="登录"
        )

        self.render("login.html",data=data)

    def post(self,*args,**kwargs):
        form = LoginForm(MultiDict(self.params))
        res = dict(code=0)
        if form.validate():
            # 验证通过
            self.set_secure_cookie("name",form.data['name'])
            res["code"] = 1
        else:
            res = form.errors
            res['code'] = 0
        self.write(res)