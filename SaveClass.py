from collections import OrderedDict
from RetryLib.ExceptionClass import *
class SaveClass():
    SaveList = []
    SaveDict = {}
    def AddList(self,centens:str or int or list or tuple or dict,Flag=False,**args)->None:
        """
        支持传入字符串、整型、浮点型、字典、元祖等等，当Falg为真时，表示
        当前列表是不可重复的，否则请填写False，该参数默认值为真。
        :param centens:
        :param Flag:
        :param args:
        :return:
        """
        self.SaveList.append(centens)
    def AddDict(self,centens:dict,Flag=False,**args):
        """
        支持传入键值对参数，当Flag为真的时候表示要求字典按顺序排列，否则将随机返回值。
        默认值为假，该函数仅用于给容器增加键值对。
        :param centens:
        :param Flag:
        :param args:
        :return:
        """
        self.SaveDict.update(centens)
    def ShowList(self):
        Save = self.SaveList
        if(len(Save)> 0):
            return Save
        else:
            print('对象为空，请先添加对象后调用！')
    def ShowDict(self):
        Save = self.SaveDict
        if (len(Save) > 0):
            return Save
        else:
            print('对象为空，请先添加对象后调用！')


class TextFexd():
    Save = SaveClass()
    _Info = ExceptionClass()
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def WriteList(self):
        if(len(self.Save.SaveList)>0):
            for item in self.Save.SaveList:
                self._Info.InfoMsg(' {} {} {}'.format(item.name,item.age,item.sex))
        else:
            print('对象为空，请先添加对象后调用！')





