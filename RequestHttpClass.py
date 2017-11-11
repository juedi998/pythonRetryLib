import requests
class RequestHttp():
    herders = {}
    session = requests.session()
    herders[
        "User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
    session.headers.update(herders)
    def Get(self,url):
        wdata = self.session.get(url,headers = self.session.headers,verify=False)
        if(wdata.status_code != 200):
            Errd = self.ErrorCode(wdata.status_code)
            raise Exception(Errd)
        else:
            wdata.encoding = 'utf8'
            return wdata
    def Post(self,url):
        wdata = self.session.post(url,headers = self.session.headers,verify=False)
        if (wdata.status_code != 200):
            Errd = self.ErrorCode(wdata.status_code)
            raise Exception(Errd)
        wdata.encoding = 'utf8'
        return wdata
    def PostForm(self,url,data):
        wdata = self.session.post(url,data=data,headers = self.session.headers,verify=False)
        if (wdata.status_code != 200):
            Errd = self.ErrorCode(wdata.status_code)
            raise Exception(Errd)
        wdata.encoding = 'utf8'
        return wdata
    def ErrorCode(self,Contens):
        dict = {
            '404':'请求失败，远端服务器返回了404错误码，该页面不存在，请纠正。',
            "500":"服务器拒绝了您的请求，返回500错误码，服务器遇到了未知错误。",
            "401":"服务器拒绝了您的请求，返回401错误码，请求未获得许可。",
            "400":"请求失败，远端服务器返回了400错误码，请检查您的请求头部。",
            "403":"请求失败，远端服务器返回了403错误码，您无权使用该网络资源。",
            "502":"请求失败，远端服务器返回了502错误码，与服务器连接超时。",
            "503":"请求失败，远端服务器返回了503错误码，服务器负荷过大，短时间内无法与服务器建立请求。",
            "000":"请求错误，远端服务器返回了未知状态码，请检查请求头部与参数。"
        }
        return dict[str(Contens)]