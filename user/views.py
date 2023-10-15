from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
# Create your views here.
#登录
def loginView(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        if User.objects.filter(username=username):
            user=authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    # msg="登录成功"
                    request.session['status']=True
                    request.session['uname']=username
                    request.session.set_expiry(300)
                    messages.success(request, "登录成功")
                
                return redirect("/index/")
            else:       
                msg="用户名密码错误"
        else:
            msg="用户名不存在"
    return render(request,"login.html",locals())        

#注册
def regView(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        email=request.POST.get("email")
        if User.objects.filter(username=username):
            msg="用户名已存在"
        else:
            user=User.objects.create_user(username=username,password=password,email=email)
            msg="注册成功"
            return redirect("/login/")
    return render(request,"register.html",locals())
def index(request):
    return  render (request,"index.html",{"name":request.session.get('uname')})

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Article
from django.contrib.auth.decorators import login_required


def view_user_articles(request):
    if not request.user.is_authenticated:
        messages.warning(request, "请先登录以访问该页面。")
        return redirect("/login/")  # 重定向到登录页面
    user = request.user  # 获取当前登录的用户
    articles = Article.objects.filter(user=user)  # 获取用户创建的所有文章
    return render(request, 'user_articles.html', {'articles': articles})

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Article

@login_required
def write(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        user = request.user  # 获取当前登录的用户

        article = Article(title=title, content=content, user=user)
        article.save()
        return HttpResponseRedirect('/write/')  # 重定向到文章列表页面或其他适当的页面

    return render(request, 'write.html', {})





    

from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from django.contrib.auth.decorators import login_required

@login_required
def edit_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        article.title = title
        article.content = content
        article.save()
        return redirect('view_user_articles')  # 重定向到用户文章列表

    return render(request, 'edit_article.html', {'article': article})


from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('/login/')  # 重定向到登录页面，你可以根据你的登录视图的名称进行调整





from django.shortcuts import render
from .models import Article

def view_published_articles(request):
    articles = Article.objects.all()  # 获取已发布的文章
    return render(request, 'published_articles.html', {'articles': articles})


from django.shortcuts import render, get_object_or_404
from .models import Article

def view_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'view_article.html', {'article': article})


def welcome(request):
    return  render (request,"welcome.html",{"name":request.session.get('uname')})