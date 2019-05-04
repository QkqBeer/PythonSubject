from django.shortcuts import render
from django.shortcuts import redirect,HttpResponse
from  io import BytesIO
from cmdb.check_code import create_validate_code
# Create your views here.
def checkCode(request):
    stream = BytesIO()
    img, code = create_validate_code()
    img.save( stream, 'PNG' )
    request.session['CheckCode'] = code
    print(str(code))
    return HttpResponse( stream.getvalue() )

def Login(request):
    error_mes=''
    if request.method=='POST':
        checkcode=request.POST.get('check_code')
        user=request.POST.get('user',None)
        psw=request.POST.get('psw',None)
        if checkcode==request.session['CheckCode']:
            if user=='root' and psw=='123':
                return redirect('/home')
            else:
                error_mes='用户名或密码错误！'
    return render(request,'Login.html',{'error_mes':error_mes})


USER_List=[{'username':'qkq','gender':'F','grade':'A'},]
def home(request):
    if request.method=='POST':
        u=request.POST.get('username')
        g=request.POST.get('gender')
        gr=request.POST.get('grade')
        temp={'username': u, 'gender': g, 'grade':gr}
        USER_List.append(temp)
        print(len(USER_List))
    return render(request,'home.html',{'USER_List':USER_List})

import os
#上传文件
def register(request):
    if request.method=='POST':
        u = request.POST.get('user')
        p = request.POST.get('psw')
        obj=request.FILES.get('picture')
        file_path=os.path.join('static/picture',obj.name)
        f=open(file_path,mode = 'wb')
        for i in obj.chunks():
            f.write(i)
        f.close()
    return render( request, 'register.html')
#两种ajax提交
def registerAjax(request):
    if request.method=='POST':
        u = request.POST.get('user')
        p = request.POST.get('psw')
        obj=request.FILES.get('picture')
        file_path=os.path.join('static/picture',obj.name)
        f=open(file_path,mode = 'wb')
        for i in obj.chunks():
            f.write(i)
        f.close()
    return HttpResponse('上传成功')
#伪ajax请求，且实现预览功能,在iframe.html
def iframe(request):
    if request.method=='GET':
        return render(request,'iframe.html')
    elif request.method=='POST':
        obj = request.FILES.get('picture')
        file_path = os.path.join( 'static/picture', obj.name )
        f = open( file_path, mode = 'wb' )
        for i in obj.chunks():
            f.write( i )
        f.close()
        dic={
            'file_path':file_path
        }
        import json
        return HttpResponse(json.dumps(dic))


from django.views import View
class Cbv(View):
    def get(self,request):
        print(request.method)
        return render(request,'cbv.html')
    def post(self,request):
        print(request.method)
        return render(request,'cbv.html')

USER_DIR= {'1':{'username':'qkq','gender':'F','grade':'A'},
           '2': {'username': 'jay', 'gender': 'F', 'grade': 'A'},
           '3': {'username': 'wxb', 'gender': 'F', 'grade': 'B'},}
def index(request):
    return render(request,'index.html',{'USER_DIR':USER_DIR})
def detail(request,uid):
    obj=USER_DIR[uid]
    return render(request,'detail.html',{"obj":obj})
userlist=[]
for i in range(100):
    userlist.append(i)
def page(request):
    p=request.GET.get('p',1)
    start=int(p)*10-10
    end=int(p)*10
    data=userlist[start:end]
    page_str=''
    f=int(len(userlist)/10)
    for i in range(1,f+1):
        str1="<a class='page' href='/cmdb/page/?p=%s'>%s</a>" %(i,i)
        page_str=page_str+str1
    return render( request, 'page.html',{'data':data , 'page_str':page_str,})
