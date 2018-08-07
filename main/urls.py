"""main URL Configuration

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
from facebook.views import play
from facebook.views import play2
from facebook.views import play3
from facebook.views import fail
from facebook.views import newsfeed
from facebook.views import detail_feed
from facebook.views import new_feed, remove_feed, edit_feed

urlpatterns = [
    path('admin/', admin.site.urls),

    path('play/', play),
    path('play2/', play2),
    path('psy/profile/', play3),

    path('fail/', fail),

    path('', newsfeed),
    # 아무것도 안넣으면 첫페이지로 이동하라는 뜻, 글자 하나라도 쓰면 마지막에 / 를 넣어야함
    path('feed/<pk>/', detail_feed),
    path('feed/<pk>/remove/', remove_feed),
    path('feed/<pk>/edit/', edit_feed),
    path('new/', new_feed),
]
