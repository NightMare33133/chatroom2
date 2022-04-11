# -*- coding: utf-8 -*-
from app.tools.form import RegistForm
from app.views.views_common import CommonHandler
from werkzeug.datastructures import MultiDict
from app.models.crud import CRUD

class RegistHandler(CommonHandler):
    def get(self,*args,**kwargs):
        data = dict(
            title="注册"
        )

        self.render("regist.html",data=data)

    def post(self,*args,**kwargs):
        form = RegistForm(MultiDict(self.params))
        res = dict(code=0)
        if form.validate():
            #验证通过
            if CRUD.save_regist_user(form):
                res["code"] = 1
        else:
            res = form.errors
            res['code'] = 0
        self.write(res)