__author__ = "那位先生Beer"
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
engine = create_engine( "mysql+pymysql://root:6988751qkq@localhost/stu",
                        encoding = 'utf-8' )
Base = declarative_base()  # 生成orm基类


class User( Base ):
    __tablename__ = 'user'  # 表名
    id = Column( Integer, primary_key = True )
    name = Column( String( 32 ) )
    password = Column( String( 64 ) )
    def __repr__( self ): #自定义返回值
        return "<User(name='%s',  password='%s')>" % (
            self.name, self.password)
Base.metadata.create_all(engine) #创建表结构

Session_class = sessionmaker( bind = engine )
# 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class()  # 生成session实例,相当于cursor的作用

my_user = Session.query( User ).filter_by( id = 4 ).first()

#在User表中查询id=1 .first()方法查询第一行，.all()返回所有查询结果
my_user.name = "Jack"
#相当于update方法，修改name
fake_user = User( name = 'Rain', password = '12345' )
Session.add( fake_user )
#添加新的条目
print( Session.query( User ).filter( User.name.in_( ['Jack', 'rain'] ) ).all() )
# 这时看session里有你刚添加和修改的数据

Session.rollback()  # 此时你rollback一下，由于默认的就是事务，所以不存入数据库

print( Session.query( User ).filter( User.name.in_( ['Jack', 'rain'] ) ).all() )
# 再查就发现刚才添加的数据没有了。
# 多条件查询objs = Session.query(User).filter(User.id>0).filter(User.id<7).all()
# 类似查询且统计 Session.query(User).filter(User.name.like("Ra%")).count()
# 分组统计 需要导入（from sqlalchemy import func）
#  Session.query(func.count(User.name),User.name).group_by(User.name).all()