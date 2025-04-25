from django.shortcuts import render

# Create your views here.
def task_list(request): # listar as tarefas cadastradas
  return

def task_detail(request, pk): # ver detalhes de uma tarefa especificada por um id (pk)
  return
  
def task_create(request): # criar uma nova tarefa
  return
    
def task_update(request, pk): # editar uma tarefa existente identificada pelo id (pk)
  return
    
def task_delete(request, pk): # deletar uma tarefa existente identificada pelo id (pk)
  return    

from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

    from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})
  
def task_create(request): # criar uma nova tarefa
  if request.method == "POST":
      form = TaskForm(request.POST)
      if form.is_valid():
          task = form.save()
          return redirect('task_detail', pk=task.pk)
  else:
      form = TaskForm()
  return render(request, 'tasks/task_form.html', {'form': form})

  from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})
  
def task_create(request): # criar uma nova tarefa
  if request.method == "POST":
      form = TaskForm(request.POST)
      if form.is_valid():
          task = form.save()
          return redirect('task_detail', pk=task.pk)
  else:
      form = TaskForm()
  return render(request, 'tasks/task_form.html', {'form': form})

  from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})
  
def task_create(request): # criar uma nova tarefa
  if request.method == "POST":
      form = TaskForm(request.POST)
      if form.is_valid():
          task = form.save()
          return redirect('task_detail', pk=task.pk)
  else:
      form = TaskForm()
  return render(request, 'tasks/task_form.html', {'form': form})

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

    from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})
  
def task_create(request): # criar uma nova tarefa
  if request.method == "POST":
      form = TaskForm(request.POST)
      if form.is_valid():
          task = form.save()
          return redirect('task_detail', pk=task.pk)
  else:
      form = TaskForm()
  return render(request, 'tasks/task_form.html', {'form': form})

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})