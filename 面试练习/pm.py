__author__ = "那位先生Beer"
import requests
from bs4 import BeautifulSoup
from pyecharts import Geo
#第一部分
#请求链接，将数据从天气网站上利用爬虫的方式下载html
respose = requests.get('https://www.tianqi.com/air/')
soup = BeautifulSoup(respose.text,'lxml')
#利用beautifulsoup css筛选器将所需数据转换成子标签列表
pmlist=soup.select('div.left614 div.main-unit div.meta ul li')
data = []
#利用属性方法将其中的所需内容转换成所需列表格式
for i in range(2,len(pmlist)):
    strList = pmlist[i].get_text('</span>').split('</span>')
    if strList[1][len(strList[1]) - 1] == '市':
        data.append((strList[1],int(strList[2])))

# #第二部分，画图部分
# geo = Geo( "全国主要城市空气质量", "data from 天气网", title_color = "#fff",
#            title_pos = "center", width = 1000,
#            height = 600, background_color = '#404a59' )
# attr, value = geo.cast( data )
# geo.add("", attr, value, visual_range = [0, 200], maptype = 'china', visual_text_color = "#fff",
#          symbol_size = 10, is_visualmap = True )
# geo.render("全国主要城市空气质量.html")  # 生成html文件


