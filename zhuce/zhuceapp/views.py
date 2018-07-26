from django.shortcuts import render,redirect
from zhuceapp.models import user
from django.http import HttpResponse
def login(request):
    return render(request,'zhuceapp/login.html')

def join(request):#注册，如果用户名已经存在就不能返回不能注册
    if  request.POST['submit']=="注册":
        if not user.objects.filter(username=request.POST['username']):
            user.objects.create(username=request.POST['username'],userpsw=request.POST['userpsw'])
            string=u"注册成功，请登录"
            return render(request,'zhuceapp/login.html',{'string': string})
        else:
            string = u"用户名已存在"
            return render(request, 'zhuceapp/joina.html', {'string': string})
def joina(request):
    return render(request,'zhuceapp/joina.html')

def islogin(request):
    if request.POST['submit']=="登录":
        u=request.POST['username']
        if user.objects.filter(username=request.POST['username']).filter(userpsw=request.POST['userpsw']):
            request.session['username'] = u #设置session
            return render(request,'zhuceapp/logined.html')
        else:
            string=u"用户名或密码错误"
            return render(request,'zhuceapp/login.html',{'string':string})
    
def xiugaimima1(request):
    return render(request,'zhuceapp/xiugaimima1.html')
def xiugaimima2(request):
    if  request.POST['submit']=="确认修改":
        if user.objects.filter(username=request.POST['username']).filter(userpsw=request.POST['userpsw']):
            a=user.objects.get(username=request.POST['username'])
            a.userpsw=request.POST['userpsw2']
            a.save()
            string = u"修改成功，请重新登录"
            return render(request,'zhuceapp/login.html',{'string': string})
def new(request):
    usr = request.session['username']#一个坑，用其他方式获取完全不行，不知道为什么
    if usr :
        string=usr
        return render(request,'zhuceapp/new.html',{'string': string})
    else:
        return render(request,'zhuceapp/login.html')
def loginout(request):
     del request.session['username']
     return render(request,'zhuceapp/login.html')
# Create your views here.
