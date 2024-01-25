"""day16 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, re_path
from app01 import views
from django.conf import settings
from django.views.static import serve
from app01.views import depart, pretty, project, user

urlpatterns = [
    path('admin/', admin.site.urls),
    # # 部门管理
    # path('depart/list/', depart.depart_list),
    # path('depart/add/', depart.depart_add),
    # path('depart/delete/', depart.depart_delete),
    # # /depart/number/edit/
    # path('depart/<int:id>/edit/', depart.depart_edit),
    # # path('test/', views.test),
    #
    # path('user/list/', user.user_list),
    # path('user/add/', user.user_add),
    # path('user/model/form/add/', user.user_model_form_add),
    # path('user/<int:id>/edit/', user.user_edit),
    # path('user/<int:id>/delete/', user.user_delete),
    #
    # path('pretty/list/', pretty.pretty_list),
    # path('pretty/add/', pretty.pretty_add),
    # path('pretty/<int:id>/delete/', pretty.pretty_delete),
    # path('pretty/<int:id>/edit/', pretty.pretty_edit),

    ####运维####
    path('devops/project/list/', project.project_list),
    path('devops/project/<int:id>/message/', project.project_message),
    path('devops/user/user_list/', user.user_list),
    path('devops/user/user_add/', user.user_model_form_add),
    path('devops/user/<int:id>/edit/', user.user_edit),
    path('devops/user/<int:id>/delete/', user.user_delete),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    path('devops/doc/<int:project_id>/list/', project.project_doc_list),
    path('devops/doc/<int:project_id>/upload/', project.project_doc_upload),
    path('devops/project/<int:id>/edit/', project.project_edit),
    path('devops/project/list/edit/', project.project_list_edit),
    path('devops/project/list/add/',project.project_list_add),
    path('devops/project/list/<int:id>/delete/',project.project_list_delete),
    path('devops/project/list/dowload/',project.file_download),
    path('devops/project/list/delete/<int:id>&project_id=<int:project_id>',project.file_delete)
]
