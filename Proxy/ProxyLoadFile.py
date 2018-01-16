from RequestHttpClass import *
from RegularClass import *
from ExceptionClass import *
import time
class ProxyClass():
    available = set()
    unavailable = set()
    _Clent = RequestHttp()
    _Retry = ExceptionClass()
    _Regular = Regular()
    def LoadIP3366(self):
        url = 'http://www.ip3366.net/?stype={}&page={}'
        header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,zh-TW;q=0.8",
            "Connection": "keep-alive",
            "DNT": "1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        }
        self._Clent.herders.update(header)
        num = 0
        while(num <= 5):
            for item in range(0,11):
                respon = self._Retry.Execute(3,self._Clent.Get,url.format(num,item))
                respon.encoding = 'gb2312'
                te = re.findall(r'<td>([\.0-9]+)</td>.*?<td>(\d{2,6})</td>',respon.text,flags=re.S)
                for i in te:
                    self.available.add(i[0] + ':' + i[1])
                print(te)
                print(self.available)
                time.sleep(2)
            num += 1
            time.sleep(2)
    def TestBaidu(self,proxyIP):
        url = "http://2017.ip138.com/ic.asp"
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,zh-TW;q=0.8",
            "Connection": "keep-alive",
            "DNT": "1",
            "Host": "2017.ip138.com",
            "Referer": "http://ip138.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        }
        self._Clent.session.proxies.update({'http':'http://202.121.178.244'})
        self._Clent.session.headers.update(headers)
        respon = self._Retry.Execute(0,self._Clent.Get,url)
        respon.encoding = 'gb2312'
        print(respon.text)

ts = ProxyClass()
ts.TestBaidu(1)

