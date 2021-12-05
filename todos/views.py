from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls.base import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Views
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
# My app
from .forms import TodoCreateForm, TodoUpdateForm
from .models import Todo


# Create your views here.
class TodoListView(LoginRequiredMixin, ListView):
    context_object_name = 'todos'
    template_name = 'todos/todo_list.html'

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)


class TodoDetailView(LoginRequiredMixin, DetailView):
    template_name = 'todos/todo_detail.html'
    context_object_name = 'todo'

    def get_object(self):
        return get_object_or_404(
            Todo, 
            user=self.request.user,
            pk=self.kwargs['pk']             
        )


class TodoCreateView(LoginRequiredMixin, CreateView):
    template_name = 'todos/todo_create.html'
    form_class = TodoCreateForm
    success_url = reverse_lazy('todo-list')
    extra_context = {
        'mode': 'create'
    }

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())


class TodoUpdateView(UpdateView):
    template_name = 'todos/todo_create.html'
    form_class = TodoUpdateForm
    extra_context = {
        'mode': 'update'
    }

    success_url = reverse_lazy('todo-list')

    def get_object(self, queryset=None):
        return get_object_or_404(
            Todo,
            pk=self.kwargs['pk'],
            user=self.request.user
        )


class TodoDeleteView(DeleteView):
    template_name = 'todos/todo_delete.html'
    success_url = reverse_lazy('todo-list')

    def get_object(self, queryset=None):
        return get_object_or_404(
            Todo,
            pk=self.kwargs['pk'],
            user = self.request.user
        )