#界面选择
import os
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
from  core import manger
from  core import teacher
from  core import student
from  core import SchoolMember
from  db  import  RW
import pickle
def main():
    SchoolMember.School.studentL = RW.readFile('student')
    SchoolMember.School.courseL = RW.readFile('course')
    SchoolMember.School.staffL = RW.readFile('staff')
    juese=input("输入你的角色：管理员M，老师T，或者学生S：")
    if juese=="M":
        manger.mangerLogin()
    elif juese=="T":
        teacher.teacherLogin()
    elif juese=="S":
        student.studentLogin()
    else:
        print("检查你的输入。。。")
    # for i in SchoolMember.School.courseL:
    #     print(i) #对象写入文件不是数据而是地址
    #     print("name %s time %s price %s" % (i.name, str(i.time),str( i.price)))
    RW.writeFile('student',SchoolMember.School.studentL)
    RW.writeFile('course', SchoolMember.School.courseL)
    RW.writeFile('staff', SchoolMember.School.staffL)
    # with open("course",'r') as f:
    #     data=pickle.loads(f.read())
    #     print(eval(data))
