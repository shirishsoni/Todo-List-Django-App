"""todolist URL Configuration

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
from django.urls import path
from todo import views as v
urlpatterns = [
    path('admin/', admin.site.urls),

    #Auth
    path('signup/',v.signupuser, name='signupuser'),
    path('logout/',v.logoutuser, name='logoutuser'),
    path('login/',v.loginuser, name='loginuser'),

    #TODO
    path('',v.home, name='home'),
    path('create/',v.createtodo, name='createtodo'),
    path('current/',v.currenttodos, name='currenttodos'),
    path('completed/',v.completedtodos, name='completedtodos'),
    path('todo/<int:todo_pk>',v.viewtodo, name='viewtodo'),
    path('todo/<int:todo_pk>/complete',v.completetodo, name='completetodo'),
    path('todo/<int:todo_pk>/delete',v.deletetodo, name='deletetodo'),

]
