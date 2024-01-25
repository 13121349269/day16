# from django import forms
# from django.shortcuts import render, redirect
# from app01 import models
# from app01.utils.pagination import Pagination
#
# def pretty_list(request):
#     """靓号列表"""
#     data_dict = {}
#     search_data = request.GET.get('q', "")
#     if search_data:
#         data_dict["mobile__contains"] = search_data
#
#     queryset = models.PrettyNum.objects.filter(**data_dict).order_by("-level")
#
#     page_object = Pagination(request, queryset)
#
#     context = {
#         "queryset": page_object.page_queryset,  # 分完页的数据
#         "search_data": search_data,
#         "page_string": page_object.html()  # 页码
#     }
#     return render(request, 'pretty/pretty_list.html', context)
#
#
# class PrettyModelForm(forms.ModelForm):
#     class Meta:
#         model = models.PrettyNum
#         fields = ['mobile', 'price', 'level', 'status']
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for name, field in self.fields.items():
#             field.widget.attrs = {"class": "form-control", "placeholder": field.label}
#
#
# def pretty_add(request):
#     """新建靓号"""
#     if request.method == "GET":
#         form = PrettyModelForm()
#         return render(request, 'pretty/pretty_add.html', {'form': form})
#
#     # 提交数据校验
#     form = PrettyModelForm(data=request.POST)
#     if form.is_valid():
#         print(form.cleaned_data)
#         form.save()
#         return redirect('/pretty/list/')
#     # 校验失败
#     return render(request, 'pretty/pretty_add.html', {"form": form})
#     # return HttpResponse('post')
#
#
# def pretty_delete(request, id):
#     """删除靓号"""
#     models.PrettyNum.objects.filter(id=id).delete()
#     return redirect('/pretty/list/')
#
#
# def pretty_edit(request, id):
#     """编辑靓号"""
#     row_object = models.PrettyNum.objects.filter(id=id).first()
#     if request.method == "GET":
#         form = PrettyModelForm(instance=row_object)
#         return render(request, 'pretty/pretty_edit.html', {'form': form})
#
#     form = PrettyModelForm(data=request.POST, instance=row_object)
#     if form.is_valid():
#         form.save()
#         return redirect('/pretty/list/')
#     return render(request, 'pretty/pretty_edit.html', {'form': form})
