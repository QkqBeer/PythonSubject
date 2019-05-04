#自定义异常
class QkqException(Exception):
    def __init__(self,mas):
        self.mas=mas
    def __str__(self):
        #return '如果一个类中定义这个__str__方法，那么在打印对象的时候，默认输出该方法的返回值'
        return self.mas
try:
    raise QkqException('异常')
except  QkqException  as e:
    print(e)
