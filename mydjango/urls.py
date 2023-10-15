"""
URL configuration for mydjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user.views import loginView,regView,index,write,view_user_articles,edit_article,view_published_articles,view_article,welcome,logout_view

urlpatterns = [
    path('',welcome),
    path('admin/', admin.site.urls),
    path('login/',loginView),
    path('reg/',regView),
    path('index/',index),
    path('write/',write),
    path('user_articles/', view_user_articles, name='view_user_articles'),
    path('edit_article/<int:article_id>/', edit_article, name='edit_article'),
    path('published_articles/', view_published_articles, name='view_published_articles'),
    path('view_article/<int:article_id>/', view_article, name='view_article'),
    path('logout/', logout_view, name='logout'),
]