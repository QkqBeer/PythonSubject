class Course:
    def __init__(self,name,price,time):
        self.name=name
        self.price=price
        self.time=time

class Student:
    def __init__(self,name,id,course,school,grade=0):
        self.name=name
        self.id=id
        self.course=course
        self.school=school
        self.grade=grade

class Teacher:
    def __init__(self,name,good,salary):
        self.name=name
        self.good=good
        self.salary=salary

class School:
    courseL=[]
    staffL=[]
    studentL=[]
    def __init__(self,name,addr):
        self.name=name
        self.addr=addr
    def addCourse(self,course):
        self.course.append(course)
        print("%s 课程添加成功"%course.name)
    def hireStaff(self,staff):
        self.staff.append(staff)
        print("%s 老师添加成功" % staff.name)
    def enroll(self,student):
        self.student.append(student)
        print("%s 学生添加成功" % student.name)
