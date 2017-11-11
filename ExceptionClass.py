import requests,time,os,traceback
class ExceptionClass():
    # _Clent = RequestHttp()
    def Execute(self,Retry,function,url,data = None):
        num = 0
        while(num < int(Retry)+1):
            try:
                if(data != None):
                    return function(url,data)
                return function(url)
            except Exception as e:
                print('请求失败，当前请求遇到问题，异常信息为：{}'.format(e))
                self.ErrorMsg(traceback.format_exc())
                time.sleep(5)
            num += 1
        print('程序在经过{}次的重试后，均无法与远程服务器正常通信，详细的错误信息已经写入到日志，请留意。'.format(Retry))
        exit()

    def InfoMsg(self,Mesg):
        fileName = '{}-InfoFile.log'.format(time.strftime('%Y-%m-%d'))
        if(os.path.exists(fileName)):
            if (int(os.path.getsize(fileName)/1024 <= 5000)):
                with open(fileName, 'a+')as df:
                    df.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "{}\n".format(Mesg))
            else:
                fileNamePath = os.path.basename(fileName)[-1]
                if(fileNamePath!='g'):
                    fileName = int(fileNamePath) + 1
                    with open(fileName, 'a+')as df:
                        df.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "{}\n".format(Mesg))
                else:
                    with open(fileName + '1', 'a+')as df:
                        df.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "{}\n".format(Mesg))
        else:
            with open(fileName, 'a+')as df:
                df.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "{}\n".format(Mesg))

    def ErrorMsg(self,ErrorMesg):
        fileName = '{}-ErrorFile.log'.format(time.strftime('%Y-%m-%d'))
        if (os.path.exists(fileName)):
            if (int(os.path.getsize(fileName)/1024 <= 5000)):
                with open(fileName,'a+')as df:
                    df.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " {}\n".format(ErrorMesg))
            else:
                fileNamePath = os.path.basename(fileName)[-1]
                if (fileNamePath != 'g'):
                    fileName = int(fileNamePath) + 1
                    with open(fileName, 'a+')as df:
                        df.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " {}\n".format(ErrorMesg))
                else:
                    with open(fileName + '1', 'a+')as df:
                        df.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " {}\n".format(ErrorMesg))
        else:
            with open(fileName, 'a+')as df:
                df.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " {}\n".format(ErrorMesg))





    # app.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
# app = ExceptionClass()
# _Clent = RequestHttp()
# ########################## 测试提交网页请求 ##########################
# def textPostForm():
#     url = r"http://www.itmaohome.com/?s=sdsd"
#     data = {
#         'ab':1
#     }
#     ss = app.Execute(3, _Clent.PostForm, url,data)
#     return ss.text
# def textPost():
#     url = r"http://www.itmaohome.com/?s=sdsd"
#     ss = app.Execute(3, _Clent.Post, url)
#     return ss.text
# def textGet():
#     url = r"http://www.itmaohome.com/?s=sdsd/45454545"
#     ss = app.Execute(3, _Clent.Get, url)
#     return ss.text
# ########################## 测试提交网页请求 ##########################
# if __name__ =='__main__':
#     test = textGet()
#     print(test)



