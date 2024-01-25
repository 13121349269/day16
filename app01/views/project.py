#-*- coding: utf-8 -*-
import os
from urllib.parse import quote
from django.core.files.storage import FileSystemStorage

from django import forms
from django.shortcuts import render, redirect, HttpResponse
from django.utils.encoding import escape_uri_path

from app01 import models
from django.http import StreamingHttpResponse, FileResponse
from wsgiref.util import FileWrapper
import hashlib


def project_list(request):
    """项目列表"""
    data = models.Project_list.objects.all()
    return render(request, 'project/project_list.html', {'data': data})


class ProListModelForm(forms.ModelForm):
    class Meta:
        model = models.Project_list
        fields = ['project_name']


def project_list_edit(request):
    """项目编辑"""
    form = models.Project_list.objects.all()
    return render(request, 'project/project_list_edit.html', {'form': form})

def project_list_add(request):
    # 添加新项目
    if request.method == "GET":
        form = ProListModelForm()
        return render(request, 'project/project_list_add.html', {'form': form})
    form = ProListModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect("/devops/project/list/edit/")
    return render(request, "project/project_list_add.html", {'form': form})


def project_list_delete(request, id):
    """删除项目"""
    models.Project_list.objects.filter(id=id).delete()
    return redirect('/devops/project/list/edit/')


class ProMsgModelForm(forms.ModelForm):
    class Meta:
        model = models.Project_Msg
        fields = ["group_coe", "project", "namespace"]


def project_message(request, id):
    """项目信息"""
    data = models.Project_Msg.objects.filter(id=id).first()
    if request.method == "GET":
        return render(request, 'project/project_message.html', {'data': data})


def project_edit(request, id):
    """项目信息编辑"""
    data = models.Project_Msg.objects.filter(id=id).first()
    if request.method == "GET":
        form = ProMsgModelForm(instance=data)
        return render(request, 'project/project_msg_edit.html', {'form': form})

    form = ProMsgModelForm(data=request.POST, instance=data)
    print(form)
    if form.is_valid():
        form.save()
        return redirect("/devops/project/{}/message/".format(id))
    return render(request, 'project/project_msg_edit.html', {'form': form})


def project_msg_delete(request, id):
    """项目信息删除"""
    models.Project_Msg.objects.filter(id=id).delete()
    return redirect('/devops/project/{}/message/'.format(id))


def project_doc_list(request, project_id):
    """项目文档列表"""
    # if request.method == "POST":
    #     file = request.FILES.get('file')
    #     set_file = models.Project_Doc(project_doc=file)
    #     set_file.save()
    doc_list = models.Project_Doc.objects.filter(project_id=project_id).all()
    # if project_id:
    #     data = models.Project_Doc.objects.filter(project_id=project_id).first()
    data = models.Project_Msg.objects.filter(project_id=project_id).first()
    return render(request, 'project/project_doc_list.html', {'doc_list': doc_list, "data": data})


class ProjectDocFrom(forms.ModelForm):
    class Meta:
        model = models.Project_Doc
        fields = ["project", "project_doc"]

    # , "project_doc"
    # def __init__(self):

from ..models import Project_Doc
def project_doc_upload(request, project_id):
    """项目文档上传"""
    # project_list = models.Project_list.objects.all()
    if request.method == "GET":
        form = ProjectDocFrom()
        return render(request, 'project/project_doc_upload.html', {"form": form})
    else:
        form = ProjectDocFrom(request.POST, request.FILES)
        file = request.FILES.get('project_doc')
        file ='project_doc/'+str(file)
        if form.is_valid():
            uploaded_file = form.save(commit=False)
            existing_file = Project_Doc.objects.filter(project_doc=file).first()
            print(Project_Doc.objects.filter(project_doc=file))
            print('-aaaaaaaaa',file,existing_file)
            if existing_file:
                # 如果存在同名文件，删除旧文件
                print('-------------')
                file_path = os.path.join(settings.MAEDIA_ROOT, str(request.FILES.get('project_doc')))
                if os.path.exists(file_path):
                    os.remove(file_path)
                # 更新数据库中的文件记录
                existing_file.delete()
                form.save()
            else:
                form.save()
            return redirect('/devops/doc/{}/list/'.format(project_id),{"form": form})


    return render(request, 'project/project_doc_list.html', {"form": form})

from django.conf import settings
def file_delete(request,id,project_id):
    """删除项目文件"""
    file_name = models.Project_Doc.objects.filter(id=id)
    print(file_name)
    file_path_query_set = file_name.filter(id=id).values_list('project_doc', flat=True)
    file_path = str(file_path_query_set[0])  # 获取 QuerySet 中的第一个元素
    file_path = file_path.strip('\'')  # 去除字符串两侧的单引号
    file_path = file_path.split('/', 1)[1]
    full_file_path = os.path.join(settings.MAEDIA_ROOT, file_path)
    file_name.delete()

    print(file_path)
    if os.path.exists(full_file_path):
        os.remove(full_file_path)
    return redirect("/devops/doc/{}/list/".format(project_id))

def file_download(request):
    # file_path = request.GET.get('file_path')
    file_name = request.GET.get('file_name')
    # file_name = os.path.basename(file_name)

    #response = StreamingHttpResponse(file_iter(file_name))  # 获取文件流
    response = FileResponse(open(file_name,'rb'))
    response['Content-Type'] = 'application/octet-stream'  # 支持所有流文件(二进制)
    response['Content-Dispositon'] = "attachment;filename*=UTF-8''{}".format(file_name)  # 下载文件名
    print(response['Content-Dispositon'])
    return response
