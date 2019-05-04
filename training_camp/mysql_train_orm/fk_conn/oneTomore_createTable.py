__author__ = "那位先生Beer"
from sqlalchemy import Integer, ForeignKey, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
engine = create_engine( "mysql+pymysql://root:6988751qkq@localhost/stu?charset=utf8",#？charset=utf-8支持中文
                        encoding = 'utf-8')
Base = declarative_base()
class Customer( Base ):
    __tablename__ = 'customer'
    id = Column( Integer, primary_key = True )
    name = Column( String (64))

    billing_address_id = Column( Integer, ForeignKey( "address.id" ) )
    shipping_address_id = Column( Integer, ForeignKey( "address.id" ) )

    billing_address = relationship( "Address" ,foreign_keys=[billing_address_id])
    shipping_address = relationship( "Address",foreign_keys=[shipping_address_id] )
    def __repr__( self ):
        return "<Customer(name='%s')>" % self.name

class Address( Base ):
    __tablename__ = 'address'
    id = Column( Integer, primary_key = True )
    street = Column( String(64) )
    city = Column( String(64) )
    state = Column( String(64) )
    def __repr__( self ):
        return "<Address(street:'%s',city:%s,state:%s)>"%(self.street ,self.city ,self.state)
Base.metadata.create_all( engine )