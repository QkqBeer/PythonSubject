from core import SchoolMember
def mangerLogin():
    while True:
        print('''---------欢迎登录管理界面-----------
                1 创建班级
                2 创建课程
                3 招收老师
                4 退出''')
        choose = input("你的选择：")
        if choose == "1":
            banji()
        elif choose == "2":
            kecheng()
        elif choose == "3":
            laoshi()
        elif choose == "4":
            break
        else:
            print("输入有问题")

def banji():
    pass
def kecheng():
    name=input("name")
    price = input("price")
    time = input("time")
    course=SchoolMember.Course(name,price,time)
    SchoolMember.School.courseL.append(course)
    print("添加成功")
def laoshi():
    name=input("name")
    good = input("good")
    salary = input("salary")
    techer=SchoolMember.Teacher(name,good,salary)
    SchoolMember.School.staffL.append(techer)
    print("添加成功")


