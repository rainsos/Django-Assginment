from django.contrib import admin
from django.urls import path  #
from todo.views import todo_list, todo_info, todo_create, todo_update, todo_delete, todo_toggle

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', todo_list, name='todo_list'),
    path('todo/<int:todo_id>/', todo_info, name='todo_info'),
    path('todo/create/', todo_create, name='todo_create'),
    path('todo/<int:todo_id>/edit/', todo_update, name='todo_update'),
    path('todo/<int:todo_id>/delete/', todo_delete, name='todo_delete'),
    path('todo/<int:todo_id>/toggle/', todo_toggle, name='todo_toggle'),
]

