__author__ = "那位先生Beer"
import pymysql

# 创建连接
conn = pymysql.connect( host = 'localhost', port = 3306, user = 'root', passwd = '6988751qkq', db = 'stu' )
# 创建游标
cursor = conn.cursor()

# 执行SQL，并返回收影响行数
effect_row = cursor.execute("insert into student (name,age,register_date) values(%s,%s,%s )",("rain",22,"2018-06-18"))
effect_row = cursor.execute("select * from student")
#取数据用游标去取cursor
print(cursor.fetchall())
# 提交，不然无法保存新建或者修改的数据
conn.commit()

# 关闭游标
cursor.close()
# 关闭连接
conn.close()