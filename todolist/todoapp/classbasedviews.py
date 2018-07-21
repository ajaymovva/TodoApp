from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from todoapp.models import *
from django.shortcuts import *
from django.urls import reverse_lazy
from todoapp.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class Todolistview(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Todo_info
    context_object_name = 'object'
    template_name = 'tododetails.html'

    def get_queryset(self):
        return Todo_info.objects.all()

    def get_context_data(self, **kwargs):
        context = super(Todolistview, self).get_context_data(**kwargs)
        # import ipdb
        # ipdb.set_trace()
        # context['data'] = self.model.objects.all()
        context.update({'user_permissions': self.request.user.get_all_permissions()})
        return context


class CreateList(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Todo_info
    form_class = Addlist
    template_name = 'todoform.html'
    success_url = reverse_lazy('todoapp:list')


class Editlist(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Todo_info
    form_class = Addlist
    template_name = 'todoform.html'
    success_url = reverse_lazy('todoapp:list')


class DeleteList(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Todo_info
    form_class = Addlist
    success_url = reverse_lazy('todoapp:list')

    def get(self, request, *args, **kwargs):
        return self.post(request, args, kwargs)
