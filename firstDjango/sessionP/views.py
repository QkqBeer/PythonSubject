from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_protect
# Create your views here.
@csrf_protect
def tijiao(request):
    if request.method=='GET':
        return  render(request,'tijiao.html')
    elif request.method=='POST':
        return HttpResponse('ok')