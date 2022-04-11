# -*- coding: utf-8 -*-
from app.views.views_user import UserHandler
from app.tools.form import UserEditForm
from werkzeug.datastructures import MultiDict
from app.models.crud import CRUD

class UserprofileHandler(UserHandler):
    def get(self,*args,**kwargs):
        data = dict(
            title="个人资料",
            user=self.user
        )

        self.render("userprofile.html",data=data)

    def post(self, *args, **kwargs):
        form = UserEditForm(MultiDict(self.params))
        res = dict(code=0)
        if form.validate():
            if CRUD.save_user(form):
                res['code'] = 1
        else:
            res = form.errors
            res["code"] = 0
        self.write(res)