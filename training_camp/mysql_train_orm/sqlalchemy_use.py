__author__ = "那位先生Beer"
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
engine = create_engine( "mysql+pymysql://root:6988751qkq@localhost/stu",
                        encoding = 'utf-8', echo = True )
#"mysql或者cx_oracle或者"（用于和数据API进行交流，根据配置文件的不同调用不同的数据库API）
#root用户名
#密码
#主机地址
#数据库
#编码方式
#是否打印sql语句
Base = declarative_base()  # 生成orm基类


class User( Base ):
    __tablename__ = 'user'  # 表名
    id = Column( Integer, primary_key = True )
    name = Column( String( 32 ) )
    password = Column( String( 64 ) )

Base.metadata.create_all(engine) #创建表结构

Session_class = sessionmaker( bind = engine )
# 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class()  # 生成session实例,相当于cursor的作用

user_obj = User( name = "alex", password = "alex3714" )  # 生成你要创建的数据对象
print( user_obj.name, user_obj.id )  # 此时还没创建对象呢，不信你打印一下id发现还是None

Session.add( user_obj )  # 把要创建的数据对象添加到这个session里， 一会统一创建
print( user_obj.name, user_obj.id )  # 此时也依然还没创建

Session.commit()  # 现此才统一提交，创建数据
