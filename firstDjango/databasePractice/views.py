from django.shortcuts import render,redirect,HttpResponse
from databasePractice.models import UserInfo,Bussiness,Host
# Create your views here.
def login(request):
    error_msg=''
    if request.method=='GET':
        return render( request, 'db_login.html', {'error_msg': error_msg} )
    elif request.method=='POST':
       u= request.POST.get('username')
       p= request.POST.get('password')
       obj=UserInfo.objects.filter(username = u,password = p).first()
       if obj:
           redir='/db/manage-'+u
           res=redirect(redir)
           res.set_cookie('username',u)
           return res
       else:
           error_msg='用户名或密码错误'
           return render( request, 'db_login.html', {'error_msg': error_msg})
    else:
        return render( request, 'db_login.html', {'error_msg': error_msg} )
#装饰器
def auth(func):
    def inner(request,username):
        if username==request.COOKIES.get('username'):
            return func(request,username)
        else:
            return redirect('/db/login')
    return inner
@auth
def manage(request,username):
        if request.method=='GET':
            BussinessList=Bussiness.objects.all()
            HostList=Host.objects.all()
            return render(request,'manage.html',{'username':username,'BussinessList':BussinessList,'HostList':HostList})
        elif request.method=='POST':
            id = request.POST.get('hid')
            if request.POST.get('option')=='del':
                Host.objects.filter(hid=id).delete()
                return HttpResponse('删除成功')
            else:
                if Host.objects.filter(hid=id).first():
                    id = request.POST.get( 'hid' )
                    n = request.POST.get( "name" )
                    i = request.POST.get( "ip" )
                    p = request.POST.get( "port" )
                    b = request.POST.get( "bid" )
                    Host.objects.filter( hid = id).update( port = p, f_id = b, Hname = n, ip = i)
                    return HttpResponse( 'ok' )
                else:
                    n = request.POST.get( "name" )
                    i = request.POST.get( "ip" )
                    p = request.POST.get( "port" )
                    b = request.POST.get( "bid" )
                    Host.objects.create(Hname=n,ip=i,port=p,f_id=b)
                    return redirect('db/manage')
def detail(request,id):
    BussinessList = Bussiness.objects.all()
    blist=Host.objects.filter(f=id)
    bobj=Bussiness.objects.filter(id=id).first()
    return render(request,'detail.html',{'blist':blist,'bobj':bobj,'BussinessList':BussinessList})


