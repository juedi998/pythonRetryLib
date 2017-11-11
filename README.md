# pythonRetryLib
这是一个基于python3的轻量级开源网络请求框架，以轻便、傻瓜式为目标，用简洁的几句代码即可获取到想要的信息，让小白也可以轻松成为爬虫大神。
该模块封装了requests第三方网络请求库，实现目的：请求网页+错误重试（可换ip重试）+日志记录功能，除库文件引用以外仅仅只需2-3句代码即可完成一个网页的请求。目前已完善请求部分，代理功能部分尚未完成封装。

示例方法（推荐）： from RetryLib.ExceptionClass import * url = "https://www.itmaohome.com" _Retry = ExceptionClass() _clent = RequestHttp() result = _Retry.Execute(3,_clent.Get,url) print(result.text)

或精简的写法（不推荐）： from RetryLib.ExceptionClass import * result = ExceptionClass().Execute(3,RequestHttp().Get,"https://www.itmaohome.com") print(result.text)

ExceptionClass.py文件中包含了两个类，其中ExceptionClass类用于处理错误重试与日志记录等，RequestHttp类用于请求网页，支持常见的Get、Post，默认已封装好头部直接按上面的方法提供参数即可，第一个Retry参数为int类型，即重试的次数，第二个为函数，将http的方法（Get或者post）传入即可（注：当函数作为参数使用时，不带小括号）第三个参数是需要请求的url地址，最后一个默认参数为data字段，如果需要传data则在第四个传入，另外如需修改Headers请求头部的时候， 可以使用字典的形式传入，方法如下： _clent.headers['xx'] = 'xx'

免责声明：本模块基于requests第三方请求库构建，使用该模块前，需先安装requests库，否则将无法使用，本模块仅供学习研究之用，如您有更好的创意或意见欢迎提出，如您使用本模块，请务必遵循开源协议！
