"""zhuce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from zhuceapp import views as zc_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',zc_views.login),
    path('islogin/',zc_views.islogin),
    path('joina/',zc_views.joina),
    path('join/',zc_views.join),
    path('xiugaimima1/',zc_views.xiugaimima1),
    path('xiugaimima2/',zc_views.xiugaimima2),
    path('new/',zc_views.new),
    path('loginout/',zc_views.loginout),
]
