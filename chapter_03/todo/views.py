from django.http import Http404
from django.shortcuts import render, redirect  # ✅ redirect 함께 import
from todo.models import Todo
from datetime import datetime


def todo_list(request):
    todo_list = Todo.objects.all().values_list('id', 'title')
    result = [{'id': todo[0], 'title': todo[1]} for i, todo in enumerate(todo_list)]
    return render(request, 'todo_list.html', {'data': result})


def todo_info(request, todo_id):
    try:
        todo = Todo.objects.get(id=todo_id)
        info = {
            'id': todo.id,
            'title': todo.title,
            'description': todo.description,
            'start_date': todo.start_date,
            'end_date': todo.end_date,
            'is_completed': todo.is_completed,
        }
        return render(request, 'todo_info.html', {'data': info})
    except Todo.DoesNotExist:
        raise Http404("Todo does not exist")


def todo_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        is_completed = request.POST.get('is_completed') == 'on'

        Todo.objects.create(
            title=title,
            description=description,
            start_date=start_date,
            end_date=end_date,
            is_completed=is_completed,
        )
        return redirect('todo_list')

    return render(request, 'todo_form.html')

def todo_update(request, todo_id):
    try:
        todo = Todo.objects.get(id=todo_id)
    except Todo.DoesNotExist:
        raise Http404("Todo does not exist")

    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')

        # 빈 문자열이면 None, 아니면 문자열을 date로 변환
        start_date_str = request.POST.get('start_date')
        end_date_str = request.POST.get('end_date')

        todo.start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date() if start_date_str else None
        todo.end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date() if end_date_str else None

        todo.is_completed = request.POST.get('is_completed') == 'on'
        todo.save()
        return redirect('todo_info', todo_id=todo.id)

    context = {'data': todo}
    return render(request, 'todo_form.html', context)

def todo_delete(request, todo_id):
    try:
        todo = Todo.objects.get(id=todo_id)
        todo.delete()
        return redirect('todo_list')
    except Todo.DoesNotExist:
        raise Http404("Todo does not exist")

def todo_toggle(request, todo_id):
    try:
        todo = Todo.objects.get(id=todo_id)
        todo.is_completed = not todo.is_completed  # 상태 반전
        todo.save()
        return redirect('todo_info', todo_id=todo.id)
    except Todo.DoesNotExist:
        raise Http404("Todo does not exist")


