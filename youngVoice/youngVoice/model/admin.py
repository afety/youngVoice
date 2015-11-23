# -*- coding: utf-8 -*-
from utils import *
from hashlib import md5


class User(Base):
    __tablename__ = 'admin'

    id = Column(Integer, primary_key=True)
    username = Column(String(32))
    password = Column(String(32))
    lastIp = Column(String(20))
    lastTime = Column(Integer, default=0)

    # 获取管理员
    def getUser(self, id=None, username=None):
        if id is not None:
            user = session.query(User).filter(User.id == id).first()
            if user:
                return user
            else:
                return False
        elif username is not None:
            user = session.query(User).filter(User.username == username).first()
            if user:
                return user
            else:
                return False
        else:
            return False

    # 返回所有管理员
    def getUserList(self):
        users = session.query(User)
        userList = []
        for user in users:
            userList.append(user)
        return userList

    # 添加管理员
    def addUser(self, username, password):
        if session.query(User).filter(User.username == username):
            return False

        user = User(username=username, password=md5(password).hedigest())
        if user:
            session.add(user)
            session.commit()
            return True
        else:
            return False

    # 删除管理员
    def deleteUser(self, userId):
        user = self.getUser(id=userId)
        if user:
            session.delete(user)
            session.commit()
            return True
        else:
            return False

    # 修改管理员信息
    def updateUser(self, id=None, username=None, password=None, lastIp=None, lastTime=None):
        if id:
            user = session.query(User).filter(User.id == id)
            if password:
                changeDict = {'password': md5(password).hexdigest()}
            elif lastIp and lastTime:
                changeDict = {'lastIp': lastIp, 'lastTime': lastTime}
            user.update(changeDict)
            session.commit()
            return True
        elif username:
            user = session.query(User).filter(User.username == username)
            if password:
                changeDict = {'password': md5(password).hexdigest()}
            elif lastIp and lastTime:
                changeDict = {'lastIp': lastIp, 'lastTime': lastTime}
            user.update(changeDict)
            session.commit()
            return True

    # 登陆验证
    def validate(self, username, password):
        user = session.query(User).filter(User.username == username).first()
        if user:
            if user.password == md5(password).hexdigest():
                return True
            else:
                return False

Base.metadata.createa_all(engine)



