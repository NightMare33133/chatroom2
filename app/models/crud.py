# -*- coding: utf-8 -*-
import datetime
from app.tools.orm import ORM
from app.models.models import User,Msg
from werkzeug.security import generate_password_hash
#增删改查的类

def dt():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
class CRUD(object):
    # 验证用户唯一性，1昵称，2邮箱，3手机
    @staticmethod
    def user_unique(data, method=1):
        # 1.调用会话
        session = ORM.db()
        user = None
        # 2.查询逻辑，事务处理
        try:
            # 执行增删改查
            model = session.query(User)
            if method == 1:
                # 验证昵称
                user = model.filter_by(name=data).first()
            if method == 2:
                # 验证邮箱
                user = model.filter_by(email=data).first()
            if method == 3:
                # 验证手机
                user = model.filter_by(phone=data).first()
        except Exception as e:
            # 发生异常回滚
            session.rollback()
        else:
            # 没有发生异常提交
            session.commit()
        finally:
            # 无论是否发生异常，关闭会话
            session.close()

        if user:
            return True
        else:
            return False

    @staticmethod
    def save_regist_user(form):
        session = ORM.db()
        try:

            user = User(
                name=form.data['name'],
                pwd=generate_password_hash(form.data['pwd']),
                email=form.data["email"],
                phone=form.data["phone"],
                sex=None,
                xingzuo=None,
                face=None,
                info=None,
                createdAt=dt(),
                updatedAt=dt()
            )

            session.add(user)
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True
    # 检测登录
    @staticmethod
    def check_login(name,pwd):
        session =  ORM.db()
        result = False
        try:
            user = session.query(User).filter_by(name=name).first()
            if user:
                if user.check_pwd(pwd):
                    result = True
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return result

    # 根据昵称查询用户
    @staticmethod
    def user(name):
        session = ORM.db()
        user = None
        try:
            user = session.query(User).filter_by(name=name).first()
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return user

    @staticmethod
    def save_user(form):
        session = ORM.db()
        try:
            user = session.query(User).filter_by(id=int(form.data['id'])).first()
            user.name = form.data['name']
            user.email = form.data['email']
            user.phone = form.data['phone']
            user.sex = int(form.data['sex'])
            user.xingzuo = int(form.data['xingzuo'])
            user.face = form.data['face']
            user.info = form.data['info']
            user.updatedAt = dt()
            session.add(user)
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True

    @staticmethod
    def save_msg(content):
        session = ORM.db()
        try:
            msg = Msg(
                content=content,
                createdAt=dt(),
                updatedAt=dt()
            )
            session.add(msg)
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True

    #加载数据库中最近的100条记录
    @staticmethod
    def lastest_msg():
        session = ORM.db()
        data = []
        try:
            data = session.query(Msg).order_by(Msg.createdAt.desc()).limit(100).all()
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return data
