__author__ = "那位先生Beer"
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
engine = create_engine( "mysql+pymysql://root:6988751qkq@localhost/stu",
                        encoding = 'utf-8')
Base = declarative_base()
class User( Base ):
    __tablename__ = 'user'  # 表名
    id = Column( Integer, primary_key = True )
    name = Column( String( 32 ) )
    password = Column( String( 64 ) )
class Address( Base ):
    __tablename__ = 'addresses'
    id = Column( Integer, primary_key = True )
    email_address = Column( String( 32 ), nullable = False )
    user_id = Column( Integer, ForeignKey( 'user.id' ) )

    user = relationship( "User", backref = "addresses" )
    # 这个nb，允许你在user表里通过backref字段反向查出所有它在addresses表里的关联项
    def __repr__( self ):
        return "<Address(email_address='%s')>" % self.email_address

Base.metadata.create_all( engine )
Session_class = sessionmaker( bind = engine )
Session = Session_class()
# email_obj = Address( email_address  = "514129067@qq.com",user_id=4)
# Session.add( email_obj )
obj = Session.query( User ).all()
for i in obj:  # 通过user对象反查关联的addresses记录
    print( i.name ,i.addresses )

addr_obj = Session.query(Address).all()
for i in addr_obj: #反向查询
    print( i.user.name )  # 在addr_obj里直接查关联的user表
Session.commit()