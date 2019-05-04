__author__ = "那位先生Beer"
from training_camp.mysql_train_orm.fk_conn import oneTomore_createTable
from sqlalchemy.orm import sessionmaker
session_class=sessionmaker(bind=oneTomore_createTable.engine)
session=session_class()
addr1=oneTomore_createTable.Address(street="Xuefudadao",city="changan",state="shanxi")
addr2=oneTomore_createTable.Address(street="xiaozhai",city="yanta",state="shanxi")
addr3=oneTomore_createTable.Address(street="wulukou",city="weiyangqu",state="shanxi")
session.add_all([addr1,addr2,addr3])
c1=oneTomore_createTable.Customer(name='qkq',billing_address=addr1,shipping_address=addr1)
c2=oneTomore_createTable.Customer(name='alex',billing_address=addr2,shipping_address=addr3)
session.add_all([c1,c2])
session.commit()

