from core import SchoolMember
def teacherLogin():
    while True:
        choose = input('''-------welcome to Oldboy teacher System------
                    1 查看学员列表
                    2 修改学员成绩
                    3 退出
    输入你的选择：
            ''')
        if choose == "1":
            chakan()
        elif choose == "2":
            xiugaichengji()
        elif choose == "3":
            break
        else:
            print("输入错误！！！")

def chakan():
    for i in SchoolMember.School.studentL:
        print(i.name, i.id, i.course, i.grade)

def xiugaichengji():
    num=int(input("输入你的选择序号："))
    stu=SchoolMember.School.studentL[num]
    print("%s 同学目前的 %s 成绩是 %s" %(stu.name,stu.course,stu.grade))
    newGrade=input("请输入新成绩：")
    SchoolMember.School.studentL[num].grade=newGrade #new value
    print("更新成功！！！")



