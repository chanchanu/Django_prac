from django.urls import path
from django.conf.urls import url
from django_app import views

urlpatterns=[
    url(r'^$', views.i, name='index'),
    #path('', views.index, name='index'), 동일한 표현 방법
]