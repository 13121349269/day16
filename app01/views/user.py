from django.shortcuts import render, redirect, HttpResponse
from app01 import models

def user_list(request):
    """用户管理"""

    # 获取用户列表
    queryset = models.UserInfo.objects.all()
    '''
    for obj in queryset:
        obj.id,obj.name.obj.password.obj.creatime.strftime("%Y-%m-%d"),obj.get_gender_display(),obj.depart.title
    '''

    return render(request, 'project_user/user_list.html', {'queryset': queryset})

def user_add(request):
    """添加用户"""

    return render(request, 'project_user/user_add.html')

###########################modelform#####################
from django import forms


class UserModelForm(forms.ModelForm):
    # 输入字符限制
    name = forms.CharField(min_length=2, label="用户名")

    class Meta:
        model = models.UserInfo
        # fields = ["name", "age", "password", "gender", "account", "create_time", "depart"]
        fields = ["name"]
        # widgets = {
        #     "name" : forms.TextInput(attrs={"class": "form-control"}),
        #     "password" : forms.PasswordInput(attrs={"class": "form-control"})
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 循环找到所有的插件，添加了class="form-control"
        for name, field in self.fields.items():
            # #某个字段不添加样式
            # if name == "password":
            #     continue
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}


def user_model_form_add(request):
    """添加用户 ModelForm"""
    if request.method == "GET":
        form = UserModelForm()
        return render(request, "project_user/user_add.html", {'form': form})

    # 用户POST提交数据，必须数据校验
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        # 保存数据
        form.save()
        return redirect('/devops/user/user_list/')
    # 校验失败，显示错误信息
    return render(request, "project_user/user_add.html", {'form': form})


def user_edit(request, id):
    """编辑用户"""
    row_object = models.UserInfo.objects.filter(id=id).first()

    if request.method == "GET":
        # 根据ID去数据库获取要编辑的那行数据
        form = UserModelForm(instance=row_object)
        return render(request, 'project_user/user_edit.html', {'form': form})

    form = UserModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        # 默认保存的是用户输入的所有数据，如果想要在用户输入以外增加一些值
        # form.instance.字段名=值
        form.save()
        return redirect('/devops/user/user_list/')
    return render(request, 'project_user/user_edit.html', {'form': form})


def user_delete(request, id):
    """删除用户"""
    models.UserInfo.objects.filter(id=id).delete()
    return redirect('/devops/user/user_list/')