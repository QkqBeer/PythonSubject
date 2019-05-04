
from pyecharts import Geo

data = [('北京',300),('上海',280),('武汉',200),('成都',190),('西安',150),('广东',270),('深圳',280),('杭州',220),('南京',180),('天津',190),('兰州',100),('重庆',180),('厦门',150)
    ]
geo = Geo("全国主要城市人工智能热度", "data from 工作岗位数", title_color="#fff", title_pos="center", width=1200, height=600,
background_color='#404a59')
attr, value = geo.cast(data)
geo.add("", attr, value, type="heatmap", is_visualmap=True, visual_range=[0, 300], visual_text_color='#fff')
geo.show_config()
geo.render()