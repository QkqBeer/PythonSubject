__author__ = "那位先生Beer"
from training_camp.mysql_train_orm.fk_conn import oneTomore_createTable
from sqlalchemy.orm import sessionmaker

session_class=sessionmaker(bind = oneTomore_createTable.engine)
session=session_class()
obj_customer=session.query(oneTomore_createTable.Customer).filter(oneTomore_createTable.Customer.name =='qkq').first()
print(obj_customer.name,obj_customer.billing_address,obj_customer.shipping_address)