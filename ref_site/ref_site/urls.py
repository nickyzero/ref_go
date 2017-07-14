"""ref_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from ref_app.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', HomeView, name="home"),
    url(r'^home/$', HomeView, name="home"),
    #회원관리
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/register/$', UserCreateView.as_view(), name='register'),
    url(r'^accounts/register/done/$', UserCreateDoneTV.as_view(), name='register_done'),
    #쇼핑리스트
    url(r'^shoppinglists/$',ShoppingListView.as_view(), name='list'),
    url(r'^shoppinglists/add/$',ShoppingListCreateView.as_view(), name='listadd'),
    url(r'^shoppinglists/(?P<pk>[0-9]+)/update/$',ShoppingListUpdateView.as_view(), name='listupdate'),
    url(r'^shopplinlists/(?P<pk>[0-9]+)/delete/$',ShoppingListDeleteView.as_view(), name='listdelete'),
    #냉장고 생성
    url(r'^ref/create/$',RefCreateView.as_view(), name='ref_create'),
    url(r'^ref/(?P<pk>\w+)/register/$',RefRegisterView.as_view(), name='ref_register'),
]
