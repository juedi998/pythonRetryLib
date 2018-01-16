import redis
from RetryLib.ExceptionClass import *
class RedisClass:
    _Log = ExceptionClass()
    def Connention(self,Hostlocal,Port,Pwd,DB='NewDB'):
        try:
            db = redis.Redis(host=Hostlocal,port=Port,password=Pwd,db=DB)
            return db
        except redis.ResponseError as e:
            print('与数据库建立链接失败，请在请求的头部加上与数据库连接的密匙。')
            self._Log.ErrorMsg("程序在与Redis缓存数据库建立连接时发生了错误，错误信息为：{}".format(e))