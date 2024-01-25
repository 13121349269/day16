from django.contrib import messages
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from app01 import models
from app01.views.project import ProListModelForm, ProMsgModelForm, ProjectDocFrom


class ProjectListView(ListView):
    model = models.Project_list
    template_name = 'project/project_list.html'
    context_object_name = 'data'


class ProjectListCreateView(CreateView):
    model = models.Project_list
    form_class = ProListModelForm
    template_name = 'project/project_list_add.html'

    def form_valid(self, form):
        messages.success(self.request, 'Project created successfully.')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('project_list_edit')


class ProjectListUpdateView(UpdateView):
    model = models.Project_list
    form_class = ProListModelForm
    template_name = 'project/project_list_edit.html'
    context_object_name = 'form'

    def form_valid(self, form):
        messages.success(self.request, 'Project updated successfully.')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('project_list_edit')


class ProjectListDeleteView(DeleteView):
    model = models.Project_list
    template_name = 'project/project_list_delete.html'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Project deleted successfully.')
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('project_list_edit')


class ProjectMessageDetailView(DetailView):
    model = models.Project_Msg
    template_name = 'project/project_message.html'
    context_object_name = 'project_msg'


class ProjectMessageUpdateView(UpdateView):
    model = models.Project_Msg
    form_class = ProMsgModelForm
    template_name = 'project/project_edit.html'
    context_object_name = 'form'

    def form_valid(self, form):
        messages.success(self.request, 'Project message updated successfully.')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('project_message', kwargs={'pk': self.object.pk})


class ProjectMessageDeleteView(DeleteView):
    model = models.Project_Msg
    template_name = 'project/project_message_delete.html'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Project message deleted successfully.')
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('project_list_edit')


class ProjectDocCreateView(CreateView):
    model = models.Project_Doc
    form_class = ProjectDocFrom #ProDocModelForm
    template_name = 'project/project_doc_upload.html'

    def form_valid(self, form):
        project_id = self.kwargs['project_id']
        project = get_object_or_404(models.Project_list, id=project_id)
        project_doc = form.save(commit=False)
        project_doc.project_id = project_id
        project_doc.save()
        messages.success(self.request, 'Document uploaded successfully.')
        return redirect('project_doc_list', project_id=project_id)


class ProjectDocListView(ListView):
    model = models.Project_Doc
    template_name = 'project/project_doc_list.html'
    context_object_name = 'project_docs'

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        return self.model.objects.filter(project_id=project_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = get_object_or_404(models.Project_list, id=self.kwargs['project_id'])
        return context