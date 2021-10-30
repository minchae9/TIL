from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect
from django.views.decorators.http import require_http_methods, require_safe, require_POST

from todo.forms import TodoForm
from .models import Todo

# Create your views here.
@require_safe
def index(request):
    tasks = get_list_or_404(Todo)
    context = {
        'tasks': tasks,
    }
    return render(request, 'todo/index.html', context)

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':    # 작성 완료
        form = TodoForm(request.POST)
        if form.is_valid():
            mission = form.save(commit=False)
            mission.done = False
            mission.save()
            return redirect('todo:index')
    else:
        form = TodoForm()
    context = {
        'form': form,
    }
    return render(request, 'todo/create.html', context)

@require_POST
def check(request, item_pk):
    item = get_object_or_404(Todo, pk=item_pk)
    if item.done:
        item.done = False
    else:
        item.done = True
    item.save()
    return redirect('todo:index')

@require_http_methods(['GET', 'POST'])
def edit(request, item_pk):
    item = get_object_or_404(Todo, pk=item_pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('todo:index')
    else:
        form = TodoForm(instance=item)
    context = {
        'form': form,
        'task': item,
    }
    return render(request, 'todo/create.html', context)

@require_POST
def delete(request, item_pk):
    item = get_object_or_404(Todo, pk=item_pk)
    item.delete()
    return redirect('todo:index')