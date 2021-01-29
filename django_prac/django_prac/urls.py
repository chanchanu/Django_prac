"""django_prac URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path
from django_app import views
from django.conf.urls import include
urlpatterns = [
    # 'name =' 이란 URL에 이름을 붙인 것으로 뷰를 식별합니다
    url(r'^django_app/',include('django_app.urls')),    # -> 내가 만든 django_app 디렉토리로 가서, 거기있는 django_app urls를 가져오는것(include)
    url(r'^$',views.index, name = 'index'), #   -> r'^$뒤에 쓰는게 주소창의 부분
    url(r'^new/',include('django_app.urls')),   # 25번줄과 26번줄의 차이는 무엇일까????
    #url(r'^new/',views.i, name = 'i'),
    #path('',views.index, name = 'index'), 같은 표현 방식
    #url(r'^$amdin/',amdin.site.urls), 같은 표현 방식
    path('admin/', admin.site.urls),
]
