import pymysql
from RetryLib.ExceptionClass import *
class MysqlClass():
    _Log = ExceptionClass()
    def Connection(self,Hostlocal,UserName,Pwd,DB='NewDB'):
        try:
            db = pymysql.connect(host=Hostlocal,user= UserName,password = Pwd,db= DB,charset='utf8')
            return db
        except Exception as e:
            self._Log.ErrorMsg('与数据库创建链接失败，请检查配置是否正确，错误信息为:{}'.format(e))
    def CreateTable(self,TableName,SqlSyntax,DBObject):
        cursor = DBObject.cursor()
        try:
            #判断表名是否存在，存在则删除，否则则创建
            cursor.execute('drop table if exists {}'.format(TableName))
            cursor.execute(SqlSyntax)
        except Exception as e:
            self._Log.ErrorMsg('创建表单失败，错误信息为:{}'.format(e))
            DBObject.rollback()
    def AddData(self,SqlSyntax,DBObject):
        cursor = DBObject.cursor()
        try:
            cursor.execute(SqlSyntax)
            DBObject.commit()
        except Exception as e:
            self._Log.ErrorMsg('插入数据失败，错误信息为:{}'.format(e))
            DBObject.rollback()
    def FindData(self,SqlSyntax,DBObject):
        cursor = DBObject.cursor()
        try:
            cursor.execute(SqlSyntax)
            results = cursor.fetchall()
            return results
        except Exception as e:
            self._Log.ErrorMsg('您查找的信息不存在，错误信息为:{}'.format(e))
    def UpdateData(self,SqlSyntax,DBObject):
        cursor = DBObject.cursor()
        try:
            cursor.execute(SqlSyntax)
            DBObject.commit()
        except Exception as e:
            self._Log.ErrorMsg('程序在试图更新数据库时出现了错误，错误信息为:{}'.format(e))
            DBObject.rollback()
    def DeleteData(self,SqlSyntax,DBObject):
        cursor = DBObject.cursor()
        try:
            cursor.execute(SqlSyntax)
            DBObject.commit()
        except Exception as e:
            self._Log.ErrorMsg('抱歉，程序在尝试删除数据时遇到了错误，该错误信息为:{}'.format(e))
            DBObject.rollback()
    def CloseDB(self,DBObject):
        try:
            DBObject.close()
        except Exception as e:
            self._Log.ErrorMsg('关闭数据库对象失败，请检查对象是否正确或正常，错误信息为:{}'.format(e))


