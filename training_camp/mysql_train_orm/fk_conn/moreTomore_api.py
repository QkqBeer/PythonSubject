__author__ = "那位先生Beer"
from training_camp.mysql_train_orm.fk_conn import moreTomore_init
from sqlalchemy.orm import sessionmaker
Session_class = sessionmaker( bind = moreTomore_init.engine )  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
s = Session_class()  # 生成session实例
#添加数据
# b1 = moreTomore_init.Book( name = "跟Alex学Python" )
# b2 =moreTomore_init. Book( name = "跟Alex学把妹" )
#
#
# a1 = moreTomore_init.Author( name = "Alex" )
# a2 = moreTomore_init. Author( name = "Jack" )
# a3 = moreTomore_init.Author( name = "Rain" )
#
# b1.authors = [a1, a2]
# b2.authors = [a1, a2, a3]
#
# s.add_all( [b1, b2,  a1, a2, a3] )
#查询
obj_author=s.query(moreTomore_init.Author).filter(moreTomore_init.Author.name=='Alex').first()
print(obj_author.books)
obj_book=s.query(moreTomore_init.Book).filter(moreTomore_init.Book.name=='跟Alex学把妹').first()
print(obj_book.authors)

s.commit()