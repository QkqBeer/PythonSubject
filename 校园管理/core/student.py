from core import SchoolMember
def studentLogin():
    list=studentZhuce()
    if list[1]:
        info=list[0]
        print("注册成功，下一步选课")
        choose=xuanke(info[2])
        if jiaofei(choose,info):
            print("Oldboy welcome to you !")
            stu=SchoolMember.Student(info[0],info[1],SchoolMember.School.courseL[choose].name,info[2])
            SchoolMember.School.studentL.append(stu)
        else:
            print("注册失败！！！")
    else:
        print("注册失败！！！")

def studentZhuce():
    print("------欢迎进入注册界面------")
    name = input("name:")
    id = input("id:")
    school = input("choose your school beijing B or shanghai S:")
    info=[name,id,school]
    return info,True

def xuanke(school):
    print("%s 学校有以下课程："%school)
    count=0
    for i in SchoolMember.School.courseL:
        print (count,i.name , i.time ,i.price)
        count+=1
    choose=int(input("输入你的选择："))
    return choose

def jiaofei(choose,info):
    course=SchoolMember.School.courseL[choose]
    print('''{}同学，请确认你的缴费选择：
            {}将共将需要你消费 {} 元'''.format(info[0],course.name,course.price))
    queren=input("确认 Y 或 取消 C")
    if queren=="Y":
        return True
    elif queren=="C":
        return False
