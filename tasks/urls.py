
# tasks/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Para views baseadas em função
    path('', views.task_list, name='task_list'), # url sem especificação de pasta já redireciona para a listagem de tarefas
    path('<int:pk>/', views.task_detail, name='task_detail'), # a identificação de cada atividade é feita por um número inteiro que é passada na url
    path('new/', views.task_create, name='task_create'), # criar uma nova tarefa
    path('<int:pk>/edit/', views.task_update, name='task_update'), # ao passar o id da tarefa seguido de edit chama a view de edição
    path('<int:pk>/delete/', views.task_delete, name='task_delete'), # ao passar o id de deleção junto com delete chama a view de deleção
    
]

