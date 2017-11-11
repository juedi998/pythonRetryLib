import re
class Regular():
    #匹配中间值
    # 参数1表示要匹配的字段，参数2为起始位置，参数3为结束位置，第四个参数为了避免过多的重复字符，需指定采集的开始与结束之间的间隔多少个字符
    def SpaceReglar(self,centons,startStr,endStr,space = 0):
        regular = r'(?<=%s)(.+?){%d}(?=%s)'%(startStr,space,endStr)
        reglar = re.search(regular,centons)
        return reglar
    #匹配数值，第一个参数为需匹配的文本，可选参数为指定的返回类型，如果适用，（某些文本中数字被文字分隔，故会被匹配多个元素，True表示返回默认，False表示将所有元素合并）
    def FilterNumberReglar(self,centons,ResultType = True):
        if(ResultType):
            regular = r'\d{1,}'
            reglar = re.findall(regular, centons, flags=re.S)
        else:
            regular = r'[[^a-zA-Z\u4e00-\u9fa5，,。？“”<《》>%\/\]\{\}\?\":；;\^&$#\@!*~\-\+_=\|（）【】‘’！￥·.]+'
            reglar = re.sub(regular,"",centons,flags=re.S)
        return reglar
    #匹配中文字符
    def FilterStrFideReglar(self,centons,ResultType = True):
        if (ResultType):
            regular = r'\w{1,}'
            reglar = re.findall(regular, centons, flags=re.S)
        else:
            regular = r'[[^0-9a-zA-Z,<>%\/\]\{\}\?\":;\^&$#\@!*~\-\+_=\|\'·.\s\n\r\t]+'
            reglar = re.sub(regular, "", centons, flags=re.S)
        return reglar
    #匹配大写字母
    def FilterUpper(self,centons,ResultType = True):
        if (ResultType):
            regular = r'\w{1,}'
            reglar = re.findall(regular, centons, flags=re.S)
        else:
            regular = r'[[^0-9a-z\u4e00-\u9fa5，,。？“”<《》>%\/\]\{\}\?\":；;\^&$#\@!*~\-\+_=\|（）【】‘’！￥·.]+'
            reglar = re.sub(regular, "", centons, flags=re.S)
        return reglar
    #匹配小写字母
    def FilterLower(self,centons,ResultType = True):
        if (ResultType):
            regular = r'\w{1,}'
            reglar = re.findall(regular, centons, flags=re.S)
        else:
            regular = r'[[^0-9A-Z\u4e00-\u9fa5，,。？“”<《》>%\/\]\{\}\?\":；;\^&$#\@!*~\-\+_=\|（）【】‘’！￥·.]+'
            reglar = re.sub(regular, "", centons, flags=re.S)
        return reglar
    #从文本最右边开始匹配
    def FilterLeft(self,centons,startStr,endStr,space = 0):
        centons = centons[::-1]
        regular = r'(?<=%s)(.+?){%d}(?=%s)' % (startStr, space, endStr)
        reglar = re.search(regular, centons)
        return reglar.group(0)[::-1]
    #从标签开始匹配
    def FilterLibelHtml(self,centons,startStr,endStr):
        regular = r'%s[.+?]?(.*?)%s' % (startStr,endStr)
        reglar = re.findall(regular,centons,flags=re.S)
        return reglar



if __name__ =='__main__':
    tes = Regular()
    htm = """
    <nav class="navcon marauto">
  <div id="mobile_nav_btn">网站导航</div>
  <div class="menu-header"><ul id="menu-%e4%b8%bb%e8%8f%9c%e5%8d%95" class="menu"><li id="menu-item-27" class="menu-item menu-item-type-custom menu-item-object-custom current-menu-item current_page_item menu-item-home menu-item-27"><a href="http://www.itmaohome.com">首页</a></li>
    <li id="menu-item-47" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-47"><a href="http://tao.itmaohome.org">微淘粉</a></li>
    <li id="menu-item-48" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-48"><a href="http://vip.itmaohome.org">微视界</a></li>
    <li id="menu-item-28" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-28"><a href="https://www.itmaohome.com/?page_id=25">微软应用程式</a>
    <ul  class="sub-menu">
	<li id="menu-item-29" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-29"><a href="https://www.itmaohome.com/?cat=2">图像处理软体</a></li>
	<li id="menu-item-30" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-30"><a href="https://www.itmaohome.com/?cat=1">微软应用程式</a></li>
	<li id="menu-item-31" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-31"><a href="https://www.itmaohome.com/?cat=3">屏幕录像</a></li>
	<li id="menu-item-32" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-32"><a href="https://www.itmaohome.com/?cat=4">网络社交软体</a></li>
	<li id="menu-item-33" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-33"><a href="https://www.itmaohome.com/?cat=5">办公软体</a></li>
	<li id="menu-item-34" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-34"><a href="https://www.itmaohome.com/?cat=6">系统工具</a></li>
    </ul>
    </li>
    <li id="menu-item-35" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-has-children menu-item-35"><a href="https://www.itmaohome.com/?cat=7">教学资源</a>
    <ul  class="sub-menu">
	<li id="menu-item-38" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-38"><a href="https://www.itmaohome.com/?cat=10">IT猫之家资源中心</a></li>
	<li id="menu-item-36" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-36"><a href="https://www.itmaohome.com/?cat=12">开源软体分享</a></li>
	<li id="menu-item-37" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-37"><a href="https://www.itmaohome.com/?cat=11">软件开发</a></li>
	<li id="menu-item-39" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-39"><a href="https://www.itmaohome.com/?cat=9">IT编程/计算机软体开发</a></li>

    """
    bb = tes.FilterLibelHtml(htm,'href="','">')
    print(bb)