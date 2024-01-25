from django.shortcuts import render, redirect, HttpResponse
from app01 import models


# Create your views here.
def depart_list(request):
    """部门列表"""
    # 数据库中获取所有的部门列表
    queryset = models.Department.objects.all()

    return render(request, 'depart/depart_list.html', {'queryset': queryset})


def depart_add(request):
    """部门添加"""
    if request.method == 'GET':
        print(request.method)
        return render(request, 'depart/depart_add.html')

    # 获取用户通过POST提交的数据
    title = request.POST.get('title')
    print(title)
    # 保存到数据库
    models.Department.objects.create(title=title)
    # 重定向回列表页面
    return redirect('/depart/list/')


def depart_delete(request):
    """删除部门"""
    # 获取id
    id = request.GET.get('id')
    # 删除数据
    models.Department.objects.filter(id=id).delete()
    return redirect('/depart/list/')


def depart_edit(request, id):
    """部门修改"""
    if request.method == 'GET':
        # 根据id获取数据
        row_object = models.Department.objects.filter(id=id).first()
        return render(request, 'depart/depart_edit.html', {'row_object': row_object})

    title = request.POST.get('title')
    models.Department.objects.filter(id=id).update(title=title)
    return redirect('/depart/list/')
