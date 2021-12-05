from django.urls import path
from . import views


urlpatterns = [
    path('', views.TodoListView.as_view(), name='todo-list'),
    path('create/', views.TodoCreateView.as_view(), name='todo-create'),
    path('update/<pk>/', views.TodoUpdateView.as_view(), name='todo-update'),
    path('delete/<pk>/', views.TodoDeleteView.as_view(), name='todo-delete'),
    path('todo/<pk>/', views.TodoDetailView.as_view(), name='todo-detail'),
]
